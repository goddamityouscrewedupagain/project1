import datetime
import uuid
import calendar

from django.db import models
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.core.validators import MinValueValidator
from django.contrib.contenttypes.fields import GenericRelation, GenericForeignKey


from dmodels.models import AbstractContentPageModel, AbstractDateTrackedModel, \
    AbstractRawContentModel, \
    AbstractDeactivatableModel, AbstractPositionedModel, DeactivatableModelQuerySet

from apps.payment.constants import SubscriptionConstants
from main.models import CustomUser


class AbstractDateTimeModel(models.Model):
    created = models.DateTimeField(_('Час створення'), auto_now_add=True)
    updated = models.DateTimeField(_('Час змінення'), auto_now=True)

    class Meta:
        abstract = True


class SoftDeletedQuerySet(models.QuerySet):

    def yes(self):
        return self.filter(is_deleted=True)

    def no(self):
        return self.filter(is_deleted=False)


class AbstractSoftDeleteModel(models.Model):
    is_deleted = models.BooleanField(_('Позначено як видалене'), default=False)
    deleted_at = models.DateTimeField(_('Час видалення'), null=True, blank=True)

    deleted = SoftDeletedQuerySet.as_manager()

    class Meta:
        abstract = True


class SubscriptionPlanFeature(
    AbstractDateTimeModel,
    AbstractDeactivatableModel,
    AbstractSoftDeleteModel
):
    """
    Model for storing plan's features, supports deactivation and soft delete abilities
    """

    name = models.CharField(_('Назва можливості'), max_length=255)
    tip = models.CharField(_('Підказка'), max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = _('Можливість тарифного плану')
        verbose_name_plural = _('Можливості тарифного плану')

    def __str__(self):
        return f'{self.name}'


class SubscriptionPlan(
    AbstractDateTimeModel,
    AbstractDeactivatableModel,
    AbstractRawContentModel,
    AbstractSoftDeleteModel
):

    features = models.ManyToManyField(
        SubscriptionPlanFeature,
        verbose_name=_('Можливості тарифного плану'),
        related_name='plan_features',
    )
    name = models.CharField(_('Назва плану'), max_length=100)
    code = models.SmallIntegerField(
        _('Аліас(код) плану'),
        choices=SubscriptionConstants.SubscriptionPlanCodes.STATUS,
        default=SubscriptionConstants.SubscriptionPlanCodes.FREE,
        unique=True
    )
    is_archive = models.BooleanField(_('Архівний'), default=False)
    is_free = models.BooleanField(_('Безкоштовний'), default=False)
    discount = models.SmallIntegerField(_('Знижка'), default=0)
    plan_color = models.CharField(_('Колір плану'), max_length=40)
    non_commercial = models.BooleanField(_('Не комерційний тариф'), default=False)

    class Meta:
        verbose_name = _('Тарифний план')
        verbose_name_plural = _('Тарифні плани')
        ordering = ['id', '-is_archive', '-active', '-is_deleted']

    def __str__(self):
        return f'{self.name}'


class PricePerPeriod(
    AbstractDateTimeModel,
    AbstractDeactivatableModel,
    AbstractSoftDeleteModel
):

    price = models.SmallIntegerField(_('Ціна'))
    period = models.SmallIntegerField(
        _('Період підписки'),
        choices=SubscriptionConstants.SubscriptionPeriods.PERIOD,
        default=SubscriptionConstants.SubscriptionPeriods.MONTH,
    )
    plan = models.ForeignKey(
        SubscriptionPlan,
        verbose_name=_('Тариф'),
        on_delete=models.DO_NOTHING,
        related_name='billing_periods',
    )

    class Meta:
        verbose_name = _('Ціна за період підписки')
        verbose_name_plural = _('Ціни за період підписки')
        ordering = ['price']

    def __str__(self):
        return f'{self.price}грн / {self.period}'

    def get_time_delta(self):
        if self.period == SubscriptionConstants.SubscriptionPeriods.WEEK:
            timedelta = datetime.timedelta(weeks=1)
        elif self.period == SubscriptionConstants.SubscriptionPeriods.MONTH:
            date = datetime.date.today()
            timedelta = datetime.timedelta(days=calendar.monthrange(date.year, date.month)[1])
        elif self.period == SubscriptionConstants.SubscriptionPeriods.YEAR:
            timedelta = datetime.timedelta(days=365)
        else:
            timedelta = datetime.timedelta(days=365*20)

        return timedelta


class SubscriptionModelQuerySet(models.QuerySet):

    def current(self):
        return self.filter(
            billed_from__lte=datetime.datetime.now(),
            billed_till__gte=datetime.datetime.now(),
        )

    def active(self):
        return self.filter(
            status=SubscriptionConstants.SubscriptionStatuses.OK
        )

    def inactive(self):
        return self.filter(
            status=SubscriptionConstants.SubscriptionStatuses.INACTIVE
        )

    def non_commercial(self):
        return self.filter(
            status=SubscriptionConstants.SubscriptionStatuses.NON_COMMERCIAL,
        )


class Subscription(
    AbstractDateTimeModel,
    AbstractDeactivatableModel,
    AbstractSoftDeleteModel
):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null=True, blank=True)
    object_id = models.PositiveIntegerField(null=True, blank=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    subscription_plan = models.ForeignKey(
        SubscriptionPlan,
        verbose_name=_('План підписки'),
        on_delete=models.DO_NOTHING,
        related_name='subscriptions',
    )
    billed_from = models.DateTimeField(_('Дата початку'), blank=True, null=True)
    billed_till = models.DateTimeField(_('Дата кінця'), blank=True, null=True)
    status = models.SmallIntegerField(
        _('Статус підписки'),
        choices=SubscriptionConstants.SubscriptionStatuses.STATUS,
        default=SubscriptionConstants.SubscriptionStatuses.PENDING,
    )
    price_per_period = models.ForeignKey(
        PricePerPeriod,
        verbose_name=_('Ціна за період'),
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True,
        default=None
    )
    is_promo = models.BooleanField(_('Промоперіод'), default=False)

    objects = SubscriptionModelQuerySet.as_manager()

    class Meta:
        verbose_name = _('Підписка')
        verbose_name_plural = _('Підписки')

    def __str__(self):
        return f'(id підписки: {self.id}), План: {self.subscription_plan}, ' \
               f'{self.content_object._meta.verbose_name}: {self.content_object.name}'

    @property
    def auto_renew(self):
        return self.content_object.auto_funds_active

    @property
    def user(self):
        return self.content_object.owner


class Payment(
    AbstractDateTimeModel,
    AbstractDeactivatableModel,
    AbstractRawContentModel,
    AbstractSoftDeleteModel
):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    user = models.ForeignKey(
        CustomUser,
        verbose_name=_('Платник'),
        related_name='payments',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    subscription = models.ForeignKey(
        Subscription,
        verbose_name=_('Платіж за таку підписку'),
        related_name='subscriptions',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    opened_at = models.DateTimeField(_('Час відкриття платежу'), default=timezone.now)
    closed_at = models.DateTimeField(_('Час закриття платежу'), blank=True, null=True)
    amount = models.PositiveIntegerField(
        _('Сума платежу'),
        default=10,
        validators=[MinValueValidator(10, _('Сума поповнення має бути 10 грн або більше'))]
    )
    is_deposit = models.BooleanField(_('Поповнення рахунку'), default=False)
    gateway_answer = models.TextField(_('Відповідь шлюза'), blank=True)
    status = models.SmallIntegerField(
        _('Статус платежу'),
        choices=SubscriptionConstants.PaymentStatuses.STATUS,
        default=SubscriptionConstants.PaymentStatuses.PENDING,
    )

    class Meta:
        verbose_name = _('Платіж')
        verbose_name_plural = _('Платежі')
        app_label = 'payment'

    def __str__(self):
        return f'{self.user}: {self.amount}грн'

    @property
    def payed_to(self):
        if self.subscription:
            return self.subscription.content_type.name
