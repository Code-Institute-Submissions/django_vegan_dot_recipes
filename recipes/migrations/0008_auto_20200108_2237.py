# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2020-01-08 22:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20200101_1900'),
    ]

    operations = [
        migrations.DeleteModel(
            name='recipe_category_name',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(default='', max_length=554),
        ),
        migrations.AlterField(
            model_name='product',
            name='recipe_category_name',
            field=models.CharField(choices=[('Starters', 'Starters'), ('Main courses', 'Main courses'), ('Desers', 'Desers'), ('Smoothies', 'Smoothies'), ('Juices', 'Juices')], default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='product',
            name='uploaded_by',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]