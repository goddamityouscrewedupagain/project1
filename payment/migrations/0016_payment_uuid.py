# Generated by Django 3.1a1 on 2020-09-07 17:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0015_auto_20200907_1724'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
