# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_bathroom'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bathroom',
            name='floor',
            field=models.IntegerField(default=0),
        ),
    ]
