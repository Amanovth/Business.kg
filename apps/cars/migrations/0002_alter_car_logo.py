# Generated by Django 5.1.1 on 2024-09-13 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='logo',
            field=models.FileField(upload_to='cars/logo'),
        ),
    ]