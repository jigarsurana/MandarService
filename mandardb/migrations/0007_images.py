# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandardb', '0006_auto_20150710_1710'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('image_id', models.AutoField(serialize=False, primary_key=True)),
                ('img', models.ImageField(upload_to=b'feeds')),
            ],
        ),
    ]
