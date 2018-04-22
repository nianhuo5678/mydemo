# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180422_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.TextField(max_length=999, null=True, blank=True),
        ),
    ]
