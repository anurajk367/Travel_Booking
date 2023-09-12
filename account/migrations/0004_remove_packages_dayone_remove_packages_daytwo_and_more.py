# Generated by Django 4.2.4 on 2023-09-05 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_travelitinerary_package'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='packages',
            name='dayone',
        ),
        migrations.RemoveField(
            model_name='packages',
            name='daytwo',
        ),
        migrations.AddField(
            model_name='packages',
            name='upcoming',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='travelitinerary',
            name='package',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='iteneries', to='account.packages'),
        ),
    ]