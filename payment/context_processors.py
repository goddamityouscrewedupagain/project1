from apps.payment.constants import SubscriptionConstants


def get_subscription_constant(constant_id):
    return SubscriptionConstants.SubscriptionPeriods.PERIOD[constant_id]
