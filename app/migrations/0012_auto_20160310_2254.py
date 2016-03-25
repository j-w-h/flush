# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160310_2236'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='shortname',
            new_name='building_url',
        ),
    ]
