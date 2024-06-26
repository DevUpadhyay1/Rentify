# Generated by Django 5.0.4 on 2024-04-28 09:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0007_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimages',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.category'),
        ),
        migrations.AddField(
            model_name='productimages',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.product'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to='product'),
        ),
    ]
