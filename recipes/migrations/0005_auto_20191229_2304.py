# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-12-29 23:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20191229_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='uploaded_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]