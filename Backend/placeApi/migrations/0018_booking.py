# Generated by Django 5.2.1 on 2025-05-30 04:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('placeApi', '0017_place_package_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('arrival_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('adults', models.PositiveIntegerField(default=1)),
                ('children', models.PositiveIntegerField(default=0)),
                ('description', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('pending', 'pending'), ('approved', 'approved'), ('cancelled', 'Cancelled')], default='pending', max_length=20)),
                ('Place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookings', to='placeApi.place')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['arrival_date'],
            },
        ),
    ]
