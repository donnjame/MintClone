# Generated by Django 3.0 on 2020-02-02 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_tracking', '0005_moneyaccount_account_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='moneyaccount',
            name='account_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]