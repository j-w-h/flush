# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_building_building_nickname'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bathroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('floor', models.FloatField(default=0)),
                ('bathroom_name', models.CharField(max_length=200)),
                ('bathroom_nickname', models.CharField(default=b'', max_length=200)),
                ('in_building', models.ForeignKey(to='app.Building')),
            ],
        ),
    ]
