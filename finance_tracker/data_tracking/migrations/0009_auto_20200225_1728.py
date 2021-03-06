# Generated by Django 3.0 on 2020-02-25 22:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('data_tracking', '0008_auto_20200225_1713'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='bill',
            managers=[
            ],
        ),
        migrations.CreateModel(
            name='MonthlyBill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('m_bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mbills', to='data_tracking.Bill')),
                ('m_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ubills', to=settings.AUTH_USER_MODEL)),
            ],
            managers=[
                ('monthly_bills_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
