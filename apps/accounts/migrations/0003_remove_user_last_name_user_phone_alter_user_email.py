# Generated by Django 5.1.1 on 2024-10-02 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_balance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='last_name',
        ),
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='Phone'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address'),
        ),
    ]