# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_user_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.TextField(max_length=499, null=True, blank=True),
        ),
    ]
