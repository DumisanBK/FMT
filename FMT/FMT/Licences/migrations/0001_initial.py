# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-31 12:59
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Licences',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Contractor_name', models.CharField(max_length=255)),
                ('Type', models.CharField(max_length=255)),
                ('issued_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiry_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'verbose_name_plural': 'Licences',
            },
        ),
    ]
