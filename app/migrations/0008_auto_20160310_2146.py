# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_building_building_shorthand'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='building_shorthand',
        ),
        migrations.AddField(
            model_name='building',
            name='building_id',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
