# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_auto_20150325_1227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_body',
            field=ckeditor.fields.RichTextField(verbose_name=b'news content'),
            preserve_default=True,
        ),
    ]
