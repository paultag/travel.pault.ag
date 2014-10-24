# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_stop_time_zone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lodging',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('rewards_account', models.CharField(max_length=128)),
                ('website', models.URLField()),
                ('phone_number', models.CharField(max_length=32)),
                ('lat', models.CharField(max_length=128)),
                ('lon', models.CharField(max_length=128)),
                ('address', models.TextField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('photo', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
