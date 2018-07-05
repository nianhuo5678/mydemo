# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180705_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name=b'reply', blank=True, to='blog.Comment', null=True),
        ),
    ]
