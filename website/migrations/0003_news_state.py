# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20150325_1200'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='state',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
