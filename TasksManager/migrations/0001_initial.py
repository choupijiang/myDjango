# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DeveloperWorkTask',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('time_elapsed_dev', models.IntegerField(default=None, null=True, verbose_name=b'Time elapsed', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title')),
                ('description', models.CharField(max_length=1000, verbose_name=b'Description')),
                ('client_name', models.CharField(max_length=1000, verbose_name=b'Client name')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name=b'Title')),
                ('description', models.CharField(max_length=1000, verbose_name=b'Description')),
                ('time_elapsed', models.IntegerField(default=None, null=True, verbose_name=b'Elapsed time', blank=True)),
                ('importance', models.IntegerField(verbose_name=b'Importance')),
                ('project', models.ForeignKey(default=None, blank=True, to='TasksManager.Project', null=True, verbose_name=b'Project')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Name', error_messages={b'required': b'You must type a name !', b'invalid': b'Wrong format.'})),
                ('phone', models.CharField(default=None, max_length=20, null=True, verbose_name=b'Phone number', blank=True)),
                ('born_date', models.DateField(default=None, null=True, verbose_name=b'Born date', blank=True)),
                ('last_connexion', models.DateTimeField(default=None, null=True, verbose_name=b'Date of last connexion', blank=True)),
                ('years_seniority', models.IntegerField(default=0, verbose_name=b'Seniority')),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='TasksManager.UserProfile')),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('userprofile_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='TasksManager.UserProfile')),
                ('specialisation', models.CharField(max_length=50, verbose_name=b'Specialisation')),
            ],
            bases=('TasksManager.userprofile',),
        ),
        migrations.AddField(
            model_name='developerworktask',
            name='task',
            field=models.ForeignKey(to='TasksManager.Task'),
        ),
        migrations.AddField(
            model_name='task',
            name='developer',
            field=models.ForeignKey(verbose_name=b'User', to='TasksManager.Developer'),
        ),
        migrations.AddField(
            model_name='developerworktask',
            name='developer',
            field=models.ForeignKey(to='TasksManager.Developer'),
        ),
        migrations.AddField(
            model_name='developer',
            name='supervisor',
            field=models.ForeignKey(verbose_name=b'Supervisor', to='TasksManager.Supervisor'),
        ),
    ]
