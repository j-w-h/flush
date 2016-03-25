# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20160310_2326'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bathroom',
            old_name='shortname',
            new_name='url',
        ),
    ]
