# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandardb', '0003_auto_20150708_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('feed_id', models.AutoField(serialize=False, primary_key=True)),
                ('feed_title', models.CharField(max_length=150)),
                ('feed_text', models.TextField()),
                ('feed_image', models.ImageField(upload_to=b'')),
                ('upload_date', models.DateField()),
                ('uploaded_by', models.CharField(max_length=100)),
            ],
        ),
    ]
