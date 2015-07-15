# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mandardb', '0004_feed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='feed_image',
            field=models.ImageField(upload_to=b'feeds'),
        ),
    ]
