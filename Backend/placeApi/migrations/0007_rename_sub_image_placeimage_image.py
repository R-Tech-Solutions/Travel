# Generated by Django 5.2.1 on 2025-05-20 05:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('placeApi', '0006_remove_placeimage_image_placeimage_sub_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='placeimage',
            old_name='sub_image',
            new_name='image',
        ),
    ]
