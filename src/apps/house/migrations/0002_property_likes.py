# Generated by Django 4.2.16 on 2024-10-10 17:51

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_house', to=settings.AUTH_USER_MODEL, verbose_name='Понравится'),
        ),
    ]