# Generated by Django 3.0 on 2020-01-30 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_tracking', '0004_auto_20200126_1706'),
    ]

    operations = [
        migrations.AddField(
            model_name='moneyaccount',
            name='account_name',
            field=models.CharField(max_length=40, null=True),
        ),
    ]
