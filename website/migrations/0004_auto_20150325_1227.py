# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_news_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='state',
            field=models.CharField(default=b'0', max_length=1, choices=[(b'1', b'Published'), (b'0', b'Draft')]),
            preserve_default=True,
        ),
    ]
