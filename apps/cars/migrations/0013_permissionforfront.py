# Generated by Django 5.1.1 on 2024-09-15 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_carcharacteristicvalue_id_car_characteristic'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionForFront',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=255, verbose_name='Key')),
                ('value', models.CharField(max_length=255, verbose_name='Value')),
            ],
        ),
    ]