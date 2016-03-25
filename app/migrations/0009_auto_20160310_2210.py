# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_auto_20160310_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathroom',
            name='rating',
            field=models.FloatField(default=0),
        ),
    ]
