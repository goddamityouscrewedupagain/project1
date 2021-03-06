# Generated by Django 3.1a1 on 2020-07-22 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('main', '0125_remove_banner_img_middle'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SubscriptionPlanFeature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Активна?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата змінення')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='Позначено як видалене')),
                ('name', models.CharField(max_length=100, verbose_name='Назва можливості')),
            ],
            options={
                'verbose_name': 'Можливість тарифного плану',
                'verbose_name_plural': 'Можливісті тарифного плану',
            },
        ),
        migrations.CreateModel(
            name='SubscriptionPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('active', models.BooleanField(default=True, verbose_name='Активна?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата змінення')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='Позначено як видалене')),
                ('name', models.CharField(max_length=100, verbose_name='Назва плану')),
                ('code', models.CharField(max_length=100, unique=True, verbose_name='Аліас плану')),
                ('is_archive', models.BooleanField(default=False, verbose_name='Архівний')),
                ('is_free', models.BooleanField(default=False, verbose_name='Безкоштовний')),
                ('discount', models.SmallIntegerField(default=0, verbose_name='Знижка')),
                ('plan_color', models.CharField(max_length=40, verbose_name='Колір плану')),
                ('features', models.ManyToManyField(related_name='_subscriptionplan_features_+', to='payment.SubscriptionPlanFeature', verbose_name='Можливості тарифного плану')),
            ],
            options={
                'verbose_name': 'Тарифний план',
                'verbose_name_plural': 'Тарифні плани',
                'ordering': ['id', '-is_archive', '-active', '-is_deleted'],
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Активна?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата змінення')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='Позначено як видалене')),
                ('auto_renew', models.BooleanField(default=False, verbose_name='Автоплатіж')),
                ('billed_from', models.DateTimeField(verbose_name='Дата початку')),
                ('billed_till', models.DateTimeField(verbose_name='Дата кінця')),
                ('pay_status', models.SmallIntegerField(choices=[(1, 'OK'), (2, 'Закінчилась'), (3, 'Безкоштовна'), (4, 'Пробний період'), (5, 'Очікування продовження')], default=3, verbose_name='Статус підписки')),
                ('is_promo', models.BooleanField(default=False, verbose_name='Промопідписка')),
                ('company', models.ManyToManyField(related_name='_subscription_company_+', to='main.Company', verbose_name='Підписка на компанію')),
                ('subscription_plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='payment.subscriptionplan', verbose_name='План підписки')),
            ],
            options={
                'verbose_name': 'Підписка',
                'verbose_name_plural': 'Підписки',
            },
        ),
        migrations.CreateModel(
            name='PricePerPeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('active', models.BooleanField(default=True, verbose_name='Активна?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата змінення')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='Позначено як видалене')),
                ('price', models.SmallIntegerField(verbose_name='Ціна')),
                ('period', models.SmallIntegerField(choices=[(1, 'Тиждень'), (2, 'Місяць'), (3, 'Рік'), (4, 'Довічно')], default=2, verbose_name='Період підписки')),
                ('plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='payment.subscriptionplan', verbose_name='Тариф')),
            ],
            options={
                'verbose_name': 'Період підписки',
                'verbose_name_plural': 'Періоди підписки',
                'ordering': ['price'],
            },
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(blank=True, verbose_name='Контент')),
                ('active', models.BooleanField(default=True, verbose_name='Активна?')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Дата змінення')),
                ('is_deleted', models.BooleanField(default=True, verbose_name='Позначено як видалене')),
                ('amount', models.SmallIntegerField(default=0, verbose_name='Сума платежу')),
                ('gateway_answer', models.TextField(blank=True, verbose_name='Відповідь шлюза')),
                ('status', models.SmallIntegerField(choices=[(1, 'Успішний'), (2, 'Провал'), (3, 'Очікування'), (4, 'Перевірка')], default=4, verbose_name='Статус платежу')),
                ('subscription_plan', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='payment.subscriptionplan', verbose_name='План підписки')),
                ('user', models.ManyToManyField(related_name='_payment_user_+', to=settings.AUTH_USER_MODEL, verbose_name='Платник')),
            ],
            options={
                'verbose_name': 'Платіж',
                'verbose_name_plural': 'Платежі',
            },
        ),
    ]
