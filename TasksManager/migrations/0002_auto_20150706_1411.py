# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TasksManager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperWorkTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_elapsed_dev', models.IntegerField(default=None, null=True, verbose_name=b'Time elapsed', blank=True)),
                ('developer', models.ForeignKey(to='TasksManager.Developer')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='app_user',
        ),
        migrations.AddField(
            model_name='developerworktask',
            name='task',
            field=models.ForeignKey(to='TasksManager.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='developers',
            field=models.ManyToManyField(to='TasksManager.Developer', through='TasksManager.DeveloperWorkTask'),
        ),
    ]
