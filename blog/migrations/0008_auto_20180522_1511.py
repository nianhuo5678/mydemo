# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20180517_1553'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='User',
            new_name='user',
        ),
    ]
