# Generated by Django 5.1.1 on 2024-10-02 13:40

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_user_language_alter_user_email_alter_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessAccount',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('tariff_plan', models.IntegerField(verbose_name='Tariff plan')),
                ('deadline', models.DateTimeField(verbose_name='Deadline')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]