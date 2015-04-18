# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_news_flickr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='news_body',
            field=ckeditor.fields.RichTextField(verbose_name=b'news content', blank=True),
            preserve_default=True,
        ),
    ]
