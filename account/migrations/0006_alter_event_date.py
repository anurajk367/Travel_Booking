# Generated by Django 4.2.4 on 2023-09-05 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(null=True),
        ),
    ]