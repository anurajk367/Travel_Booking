# Generated by Django 4.2.4 on 2023-09-11 08:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0009_rename_address_intrested_message_intrested_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booked',
            name='user',
            field=models.ForeignKey(default=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
