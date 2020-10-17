# Generated by Django 3.1a1 on 2020-08-01 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_auto_20200801_1632'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час видалення'),
        ),
        migrations.AddField(
            model_name='priceperperiod',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час видалення'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час видалення'),
        ),
        migrations.AddField(
            model_name='subscriptionplan',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час видалення'),
        ),
        migrations.AddField(
            model_name='subscriptionplanfeature',
            name='deleted_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Час видалення'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Час змінення'),
        ),
        migrations.AlterField(
            model_name='priceperperiod',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='priceperperiod',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Час змінення'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Час змінення'),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='subscriptionplan',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Час змінення'),
        ),
        migrations.AlterField(
            model_name='subscriptionplanfeature',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Час створення'),
        ),
        migrations.AlterField(
            model_name='subscriptionplanfeature',
            name='updated',
            field=models.DateTimeField(auto_now=True, verbose_name='Час змінення'),
        ),
    ]