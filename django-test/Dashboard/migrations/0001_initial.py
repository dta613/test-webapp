# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('Patient_name', models.CharField(max_length=60)),
                ('age', models.PositiveSmallIntegerField()),
                ('location', models.CharField(max_length=30)),
                ('condition', models.CharField(max_length=150)),
                ('medication', models.CharField(max_length=30)),
                ('initial_visit', models.DateField()),
                ('followup_appt', models.DateField()),
                ('reminder_freq', models.PositiveSmallIntegerField()),
            ],
        ),
    ]
