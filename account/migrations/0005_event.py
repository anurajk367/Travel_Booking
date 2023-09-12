# Generated by Django 4.2.4 on 2023-09-05 11:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_remove_packages_dayone_remove_packages_daytwo_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventname', models.CharField(max_length=300)),
                ('date', models.DateField()),
                ('package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='account.packages')),
            ],
        ),
    ]