# Generated by Django 5.1.1 on 2024-10-01 09:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_posts', '0008_carsposts_is_active'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='carsposts',
            name='likes',
            field=models.ManyToManyField(null=True, related_name='liked_posts', to=settings.AUTH_USER_MODEL, verbose_name='Понравится'),
        ),
    ]