# Generated by Django 5.2.1 on 2025-06-03 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeApi', '0022_booking_children_ages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, max_length=255, null=True, upload_to='items/images/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
