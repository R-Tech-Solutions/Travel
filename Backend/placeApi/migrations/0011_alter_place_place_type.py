# Generated by Django 5.2.1 on 2025-05-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeApi', '0010_alter_place_place_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='place',
            name='place_type',
            field=models.CharField(choices=[('trending', 'Trending Places'), ('adventure', 'Adventure Places'), ('Hiking', 'Hiking & Trekking Places'), ('Leisure', 'Leisure Travel Places')], default='trending', max_length=50),
        ),
    ]
