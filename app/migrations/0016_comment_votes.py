# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_bathroom_picture_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='votes',
            field=models.IntegerField(default=0),
        ),
    ]
