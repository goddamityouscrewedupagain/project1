from django.urls import path, register_converter

from apps.payment.views import payment_history, company_subscribe_plans, choose_payment, \
    PayView, PayCallbackView, subscription_success, payment_failed, payment_deposit, no_money, \
    deposit_success
from main import converters

app_name = "payment"
uuid = '/^[0-9A-F]{8}-[0-9A-F]{4}-4[0-9A-F]{3}-[89AB][0-9A-F]{3}-[0-9A-F]{12}$/i'

register_converter(converters.SlugOrNotConverter, "slug_or_not")

urlpatterns = [
    # payment
    path('pay/', PayView.as_view(), name='pay'),
    path('pay-callback/', PayCallbackView.as_view(), name='pay_callback'),

    # pages
    path('payment/<slug_or_not:payment_uuid>/choose', choose_payment, name="choose_payment"),
    path('payment/<slug_or_not:payment_uuid>/success', subscription_success, name="subscription_success"),
    path('payment/<slug_or_not:payment_uuid>/deposit-success', deposit_success, name="deposit_success"),
    path('payment/<slug_or_not:payment_uuid>/failed', payment_failed, name="payment_failed"),
    path('payment/<slug_or_not:payment_uuid>/no-money', no_money, name="no_money"),

    path('<slug_or_not:username>/deposit', payment_deposit, name="payment_deposit"),
    path('<slug_or_not:slug>/plans', company_subscribe_plans,
         name="company_subscribe_plans"),
    path('<slug_or_not:username>/payment-history/', payment_history, name="payment_history"),
]
