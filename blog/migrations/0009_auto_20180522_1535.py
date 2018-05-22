# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180522_1511'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('id',)},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',)},
        ),
    ]
