# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=2, choices=[(b'XQ', b'\xe9\x9c\x80\xe6\xb1\x82'), (b'WT', b'\xe9\x97\xae\xe9\xa2\x98')])),
                ('statu', models.CharField(max_length=2, choices=[(b'CG', b'\xe5\xb8\xb8\xe8\xa7\x84'), (b'JJ', b'\xe7\xb4\xa7\xe6\x80\xa5'), (b'TJ', b'\xe7\x89\xb9\xe7\xba\xa7')])),
                ('uat_date', models.DateField(null=True, blank=True)),
                ('publish_date', models.DateField(null=True, blank=True)),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100)),
                ('description', models.CharField(max_length=100, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d')),
                ('description', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-add_date',),
            },
        ),
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=100, verbose_name=b'\xe7\x89\x88\xe6\x9c\xac\xe5\x8f\xb7')),
                ('description', models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x8f\x8f\xe8\xbf\xb0', blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-add_date',),
            },
        ),
        migrations.AddField(
            model_name='content',
            name='actual_version',
            field=models.ForeignKey(related_name='actual_version', to='amazingTable.Version'),
        ),
        migrations.AddField(
            model_name='content',
            name='developer',
            field=models.ManyToManyField(related_name='developer', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='module',
            field=models.ManyToManyField(to='amazingTable.Module'),
        ),
        migrations.AddField(
            model_name='content',
            name='plan_version',
            field=models.ForeignKey(related_name='plan_version', to='amazingTable.Version'),
        ),
        migrations.AddField(
            model_name='content',
            name='product_manager',
            field=models.ForeignKey(related_name='product_manager', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='content',
            name='project',
            field=models.ForeignKey(to='amazingTable.Project'),
        ),
        migrations.AddField(
            model_name='content',
            name='tester',
            field=models.ManyToManyField(related_name='tester', to=settings.AUTH_USER_MODEL),
        ),
    ]
