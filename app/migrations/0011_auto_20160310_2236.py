# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160310_2224'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bathroom',
            old_name='nickname',
            new_name='shortname',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='nickname',
            new_name='shortname',
        ),
    ]
