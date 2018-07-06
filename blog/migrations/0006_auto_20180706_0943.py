# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180705_1705'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=mptt.fields.TreeForeignKey(related_name='children', verbose_name=b'\xe5\xbc\x95\xe7\x94\xa8', blank=True, to='blog.Comment', null=True),
        ),
    ]
