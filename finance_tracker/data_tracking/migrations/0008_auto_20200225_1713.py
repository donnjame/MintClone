# Generated by Django 3.0 on 2020-02-25 22:13

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('data_tracking', '0007_auto_20200225_1657'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bill',
            managers=[
                ('monthly_bills_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
