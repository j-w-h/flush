# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20160310_2210'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bathroom',
            old_name='bathroom_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='bathroom',
            old_name='bathroom_nickname',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='building_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='building_id',
            new_name='nickname',
        ),
        migrations.RenameField(
            model_name='building',
            old_name='building_nickname',
            new_name='picture_url',
        ),
        migrations.RemoveField(
            model_name='building',
            name='building_picture_url',
        ),
    ]
