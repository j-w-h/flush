# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20160310_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='building',
            old_name='building_url',
            new_name='url',
        ),
    ]
