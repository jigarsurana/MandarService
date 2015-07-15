# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('mandardb', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='landline1',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?\\d{10,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='person',
            name='landline2',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?\\d{10,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile1',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?\\d{10,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='person',
            name='mobile2',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?\\d{10,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='person',
            name='office1',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?\\d{10,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
        migrations.AlterField(
            model_name='person',
            name='office2',
            field=models.CharField(max_length=15, validators=[django.core.validators.RegexValidator(regex=b'^\\+?\\d{10,15}$', message=b"Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")]),
        ),
    ]
