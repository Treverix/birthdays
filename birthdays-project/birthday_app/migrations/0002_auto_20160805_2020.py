# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-05 20:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthdate',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='first_name',
            field=models.CharField(max_length=20, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='last_name',
            field=models.CharField(max_length=30, verbose_name='Last Name'),
        ),
    ]