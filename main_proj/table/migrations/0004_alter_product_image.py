# Generated by Django 5.0.4 on 2024-04-27 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('table', '0003_alter_product_edate_alter_product_sdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
