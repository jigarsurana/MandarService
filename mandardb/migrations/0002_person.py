# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandardb', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(serialize=False, primary_key=True)),
                ('first_name', models.CharField(max_length=80)),
                ('middle_name', models.CharField(max_length=80)),
                ('last_name', models.CharField(max_length=80)),
                ('mobile1', models.PositiveIntegerField()),
                ('mobile2', models.PositiveIntegerField()),
                ('landline1', models.PositiveIntegerField()),
                ('landline2', models.PositiveIntegerField()),
                ('office1', models.PositiveIntegerField()),
                ('office2', models.PositiveIntegerField()),
                ('home_address', models.ForeignKey(related_name='home_add', to='mandardb.Address')),
                ('office_address', models.ForeignKey(related_name='off_add', to='mandardb.Address')),
            ],
        ),
    ]
