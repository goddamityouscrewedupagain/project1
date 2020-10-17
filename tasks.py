from django.apps import apps

from bodia.celery import app
from payment.constants import SubscriptionConstants
from payment.utils import renew_subscription, get_free_subscription


@app.task
def send_payment_reminder(days_left, to, expired=False):
    from django.core.mail import EmailMessage
    from django.template.loader import render_to_string
    from django.utils.translation import ugettext_lazy as _

    if expired:
        topic = _('Ваша підписка на Bodia завершилась.')
        message = render_to_string('payment/mail/payment_reminder.html', {
            'expired': expired,
        })
    else:
        topic = _('Нагадування про необхідність продовження підписки на Bodia')
        message = render_to_string('payment/mail/payment_reminder.html', {
            'days': days_left,
        })

    email = EmailMessage(topic, message, to=[to])
    email.send()


@app.task
def inspect_subscriptions():
    from datetime import datetime
    from apps.payment.constants import SubscriptionConstants

    SubscriptionPlan = apps.get_model('payment', 'SubscriptionPlan')
    Subscription = apps.get_model('payment', 'Subscription')

    # for now we have only these reminders:
    five_days_reminder = True
    one_day_reminder = True
    expired_reminder = True

    days_to_remind = [5, 1, ]  # we have these days to remind for now
    days_to_renew = 1  # we have each 1 day renew period for now

    active_subscriptions = Subscription.objects.active()
#    change subs statuses and send notifs
    for subscription in active_subscriptions:
        delta = datetime.date(subscription.billed_till) - datetime.now().date()

        # process auto payments only if enabled in project conf
        if subscription.auto_renew and delta.days < days_to_renew:
            renewed = renew_subscription(subscription)
            if renewed:
                continue

        elif subscription.billed_till < datetime.now():
            print(subscription)
            # subscription is over:
            subscription.status = SubscriptionConstants.SubscriptionStatuses.INACTIVE

            new_subscription = subscription\
                .content_object\
                .subscriptions\
                .current()\
                .inactive()\
                .order_by('-subscription_plan__code')\
                .first()
            new_subscription = new_subscription or get_free_subscription(subscription.content_object)
            new_subscription.status = SubscriptionConstants.SubscriptionStatuses.OK
            new_subscription.save()
            subscription.save()
            send_payment_reminder.delay(
                delta.days,
                subscription.content_object.user.email,
                expired=True,
            )

        # elif delta.days in days_to_remind:
        #     send_payment_reminder.delay(delta.days, subscription.content_object.user.email)
