# Generated by Django 4.2.4 on 2023-09-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_booked'),
    ]

    operations = [
        migrations.AddField(
            model_name='packages',
            name='image2',
            field=models.ImageField(default='default_image.jpg', upload_to='package_images'),
        ),
        migrations.AddField(
            model_name='packages',
            name='image3',
            field=models.ImageField(default='default_image.jpg', upload_to='package_images'),
        ),
    ]