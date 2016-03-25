# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_building_building_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='building_shorthand',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
