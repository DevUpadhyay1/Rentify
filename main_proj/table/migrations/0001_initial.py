# Generated by Django 5.0.4 on 2024-04-25 19:45

import django.db.models.deletion
import table.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100, null=True)),
                ('status', models.BooleanField(default=False)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Address',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('pid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=table.models.user_directory_path)),
                ('descrption', models.TextField(blank=True, default='This is a product', null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('specification', models.TextField(blank=True, null=True)),
                ('product_status', models.CharField(choices=[('in_review', 'In Review'), ('rejected', 'Rejected')], max_length=10)),
                ('status', models.BooleanField(default=True)),
                ('sdate', models.DateField(auto_now_add=True)),
                ('edate', models.DateField(auto_now_add=True)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.category')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('tags', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.tags')),
            ],
            options={
                'verbose_name_plural': 'Product',
            },
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(upload_to='prduct-images')),
                ('date', models.DateField(auto_now_add=True)),
                ('Category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.category')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.product')),
            ],
            options={
                'verbose_name_plural': 'Product_images',
            },
        ),
        migrations.CreateModel(
            name='ProductReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review', models.TextField()),
                ('Rating', models.IntegerField(choices=[('1', '★☆☆☆☆'), ('2', '★★☆☆☆'), ('3', '★★★☆☆'), ('4', '★★★★☆'), ('5', '★★★★★')], default=None)),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Product Review',
            },
        ),
        migrations.CreateModel(
            name='Renter',
            fields=[
                ('rid', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to=table.models.user_directory_path)),
                ('descrption', models.TextField(blank=True, null=True)),
                ('address', models.CharField(max_length=100)),
                ('contact', models.CharField(max_length=100)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Renter',
            },
        ),
        migrations.CreateModel(
            name='Product_availibility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availibility', models.BooleanField(default=False)),
                ('sdate', models.DateField(auto_now_add=True)),
                ('edate', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.product')),
                ('renter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.renter')),
            ],
            options={
                'verbose_name_plural': 'Product Avilibility',
            },
        ),
        migrations.CreateModel(
            name='wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='table.product')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'wishlists',
            },
        ),
    ]