# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(serialize=False, primary_key=True)),
                ('line1', models.CharField(max_length=50)),
                ('line2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=40)),
                ('zipcode', models.CharField(max_length=10)),
                ('country', models.CharField(max_length=2, verbose_name=b'2 Digit ISO')),
            ],
        ),
    ]
