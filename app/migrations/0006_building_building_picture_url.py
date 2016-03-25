# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20160310_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='building_picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
