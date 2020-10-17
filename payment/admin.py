from django.contrib import admin
from django.db.models import Q
from django.utils.safestring import mark_safe
from django.utils.translation import ugettext_lazy as _

from apps.payment.models import PricePerPeriod, SubscriptionPlanFeature, SubscriptionPlan, Payment, \
    Subscription


def admin_method_attributes(**outer_kwargs):
    """
    Wrap an admin method with passed arguments as attributes and values.
    DRY way of extremely common admin manipulation such as setting
    short_description, allow_tags, etc.
    """

    def method_decorator(func):
        for kw, arg in outer_kwargs.items():
            setattr(func, kw, arg)
        return func

    return method_decorator


def switch_active(modeladmin, request, queryset):
    queryset.update(active=Q(active=False))


class SubscriptionAdmin(admin.ModelAdmin):
    save_on_top = True
    actions_on_top = True
    save_as = True
    list_per_page = 50
    actions = [switch_active, ]
    ordering = ('-created',)
    switch_active.short_description = _('Активувати/Деактивувати вибрані елементи')


@admin.register(PricePerPeriod)
class PricePerPeriodAdmin(SubscriptionAdmin):
    readonly_fields = [
        'created',
        'updated',
    ]
    list_display = [
        'id',
        'price',
        'period',
        'plan',
        'active',
        'updated',
        'created',
    ]

    list_filter = [
        'active',
        'created',
        'updated',
        'period',
        'plan',
    ]
    search_fields = [
        'period',
        'price',
    ]
    fieldsets = [
        (
            _('Основні поля'), {
                'fields': [
                    'price',
                    'period',
                    'plan',
                    'active',
                ]
            }
        ),
        (
            _('Мета інформація'), {
                'fields': [
                    'created',
                    'updated',
                ]
            }
        ),
    ]


@admin.register(SubscriptionPlanFeature)
class SubscriptionPlanFeatureAdmin(SubscriptionAdmin):
    readonly_fields = [
        'created',
        'updated',
    ]
    list_display_links = ['id', 'name', ]
    list_display = [
        'id',
        'name',
        'active',
        'updated',
        'created',
    ]

    list_filter = [
        'active',
        'created',
        'updated',
        # 'period',
    ]
    search_fields = [
        'name',
    ]
    fieldsets = [
        (
            _('Основні поля'), {
                'fields': [
                    'name',
                    'active',
                ]
            }
        ),
        (
            _('Мета інформація'), {
                'fields': [
                    'created',
                    'updated',
                ]
            }
        ),
    ]


@admin.register(SubscriptionPlan)
class SubscriptionPlanAdmin(SubscriptionAdmin):
    readonly_fields = [
        'created',
        'updated',
    ]
    list_display_links = ['id', 'name', ]
    list_display = [
        'id',
        'name',
        'code',
        'is_free',
        'discount',
        'is_deleted',
        'active',
        'updated',
        'created',
    ]

    list_filter = [
        'is_deleted',
        'active',
        'created',
        'updated',
    ]
    search_fields = [
        'name',
    ]
    fieldsets = [
        (
            _('Основні поля'), {
                'fields': [
                    'name',
                    'discount',
                    'code',
                    'features',
                    'is_deleted',
                    'active',
                    'is_free',
                    'non_commercial',
                ]
            }
        ),
        (
            _('Додатково'), {
                'fields': [
                    'is_archive',
                    'plan_color',
                    'content',
                ]
            }
        ),
        (
            _('Мета інформація'), {
                'fields': [
                    'created',
                    'updated',
                ]
            }
        ),
    ]


@admin.register(Payment)
class PaymentAdmin(SubscriptionAdmin):
    # form = CustomUserAutocompleteForm
    readonly_fields = [
        'id',
        'opened_at',
        'closed_at',
    ]
    list_display_links = ['id', 'user', ]
    list_display = [
        'id',
        'user',
        'amount',
        'is_deposit',
        'status',
        'is_deleted',
        'active',
        'closed_at',
        'opened_at',
    ]
    list_filter = [
        'is_deleted',
        'is_deposit',
        'status',
        'active',
        'opened_at',
        'closed_at',
    ]
    search_fields = [
        'amount',
        'gateway_answer',
    ]
    fieldsets = [
        (
            _('Основні поля'), {
                'fields': [
                    'id',
                    'amount',
                    'is_deposit',
                    'status',
                    'subscription',
                    'user',
                    'is_deleted',
                    'active',
                ]
            }
        ),
        (
            _('Додатково'), {
                'fields': [
                    'gateway_answer',
                ]
            }
        ),
        (
            _('Мета інформація'), {
                'fields': [
                    'opened_at',
                    'closed_at',
                ]
            }
        ),
    ]


@admin.register(Subscription)
class SubscriptionAdmin(SubscriptionAdmin):
    readonly_fields = [
        'id',
        'created',
        'updated',
    ]
    list_display = [
        'id',
        'related_object',
        'subscription_plan',
        'status',
        'billed_from',
        'billed_till',
    ]

    list_filter = [
        'is_promo',
        'status',
        'is_deleted',
        'active',
        'created',
        'updated',
        'billed_from',
        'billed_till',
    ]
    search_fields = [
        'subscription_plan__code',
        'subscription_plan__name',
    ]
    fieldsets = [
        (
            _('Основні поля'), {
                'fields': [
                    'id',
                    'status',
                    'subscription_plan',
                    'billed_from',
                    'billed_till',
                    'is_promo',
                    'active',
                    'is_deleted',
                ]
            }
        ),
        (
            _('Мета інформація'), {
                'fields': [
                    'created',
                    'updated',
                ]
            }
        ),
    ]

    def related_object(self, object):
        return object.content_object.name
