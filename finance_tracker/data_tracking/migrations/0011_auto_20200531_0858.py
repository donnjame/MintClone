# Generated by Django 3.0 on 2020-05-31 12:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_tracking', '0010_delete_monthlybill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bill',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_bills', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='moneyaccount',
            name='user',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='user_accounts', to=settings.AUTH_USER_MODEL),
        ),
    ]
