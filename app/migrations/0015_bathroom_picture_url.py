# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160310_2345'),
    ]

    operations = [
        migrations.AddField(
            model_name='bathroom',
            name='picture_url',
            field=models.CharField(default=b'', max_length=200),
        ),
    ]
