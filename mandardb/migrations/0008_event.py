# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandardb', '0007_images'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.AutoField(serialize=False, primary_key=True)),
                ('event_name', models.CharField(max_length=150)),
                ('event_venue', models.CharField(max_length=150)),
                ('event_date', models.DateField()),
                ('event_time', models.DateField()),
                ('event_by', models.CharField(max_length=150)),
                ('event_image', models.URLField()),
            ],
        ),
    ]
