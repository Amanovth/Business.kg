# Generated by Django 5.1.1 on 2024-10-03 11:16

import django.db.models.deletion
import versatileimagefield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars_posts', '0010_alter_carsposts_likes'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pictures',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pictures', versatileimagefield.fields.VersatileImageField(upload_to='car/user/pictures/list/')),
                ('cars', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cars_pictures', to='cars_posts.carsposts')),
            ],
            options={
                'verbose_name': 'Фотография',
                'verbose_name_plural': 'Фотографии',
            },
        ),
    ]