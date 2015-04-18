# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_body',
            field=models.TextField(verbose_name=b'news content'),
            preserve_default=True,
        ),
    ]
