# Generated by Django 5.0.4 on 2024-05-06 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0010_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='days',
            field=models.DecimalField(decimal_places=3, default=0, max_digits=10, null=True),
        ),
    ]
