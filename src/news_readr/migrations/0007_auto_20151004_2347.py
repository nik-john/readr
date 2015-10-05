# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news_readr', '0006_auto_20151004_2346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img_primary',
            field=models.ImageField(default=b'../static/news_readr/img/404.jpg', null=True, upload_to=b'img', blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='img_secondary',
            field=models.ImageField(default=b'../static/news_readr/img/404.jpg', null=True, upload_to=b'', blank=True),
        ),
    ]
