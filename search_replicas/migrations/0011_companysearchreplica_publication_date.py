# Generated by Django 3.1a1 on 2020-08-31 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search_replicas', '0010_auto_20200714_1701'),
    ]

    operations = [
        migrations.AddField(
            model_name='companysearchreplica',
            name='publication_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
