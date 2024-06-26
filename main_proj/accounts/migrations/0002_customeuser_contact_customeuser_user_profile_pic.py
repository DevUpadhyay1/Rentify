# Generated by Django 5.0.4 on 2024-04-26 14:22

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customeuser',
            name='contact',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='customeuser',
            name='user_profile_pic',
            field=models.ImageField(default='images/default.jpeg', upload_to=accounts.models.user_directory_path),
        ),
    ]
