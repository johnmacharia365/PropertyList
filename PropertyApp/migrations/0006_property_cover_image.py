# Generated by Django 5.2 on 2025-05-11 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PropertyApp', '0005_alter_propertyimage_cover_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='cover_image',
            field=models.ImageField(default='property_images/list.jpeg', upload_to='property_images/'),
        ),
    ]
