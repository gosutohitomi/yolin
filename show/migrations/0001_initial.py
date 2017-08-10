# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-08-10 04:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seconds', models.IntegerField(default=0)),
                ('publication_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
