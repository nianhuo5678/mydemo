# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.TextField(max_length=50)),
                ('content', models.TextField(max_length=2000)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField(max_length=500)),
                ('pub_date', models.DateField(default=django.utils.timezone.now)),
                ('article', models.ForeignKey(to='blog.Article')),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='info',
            field=models.TextField(max_length=300, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.TextField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(to='blog.User'),
        ),
        migrations.AddField(
            model_name='article',
            name='User',
            field=models.ForeignKey(to='blog.User'),
        ),
    ]
