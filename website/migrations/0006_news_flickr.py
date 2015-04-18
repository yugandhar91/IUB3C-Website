# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20150406_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='flickr',
            field=models.CharField(default=b'0', max_length=50),
            preserve_default=True,
        ),
    ]
