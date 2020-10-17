# from dal import autocomplete

from django import forms
from django.forms.utils import ErrorList

from apps.payment.models import Subscription, Payment


class SubscribeForm(forms.ModelForm):
    billing_period = forms.CharField(widget=forms.RadioSelect())
    signature = forms.CharField(required=False, widget=forms.HiddenInput())
    data = forms.CharField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = Subscription
        fields = [
            'signature',
            'data',
            'subscription_plan',
            'billing_period'
        ]


class ChoosePaymentForm(forms.ModelForm):
    payment_type = forms.CharField(widget=forms.RadioSelect())

    class Meta:
        model = Subscription
        fields = [
            'payment_type',
        ]


class PaymentDepositForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', ]




