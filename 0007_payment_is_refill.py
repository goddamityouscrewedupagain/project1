# Generated by Django 3.1a1 on 2020-08-02 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0006_auto_20200801_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='is_refill',
            field=models.BooleanField(default=False, verbose_name='Поповнення рахунку'),
        ),
    ]
