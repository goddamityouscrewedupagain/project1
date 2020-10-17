import os

from celery import Celery
from django.conf import settings

from manage import DEFAULT_DJANGO_SETTINGS_MODULE

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', DEFAULT_DJANGO_SETTINGS_MODULE)

app = Celery('bodia')
CELERY_TIMEZONE = settings.TIME_ZONE
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

