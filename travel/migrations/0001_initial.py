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
            name='Leg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=128)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ServiceProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('rewards_account', models.CharField(max_length=128)),
                ('website', models.URLField()),
                ('phone_number', models.CharField(max_length=32)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=16)),
                ('lat', models.CharField(max_length=128)),
                ('lon', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('reason', models.TextField()),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='leg',
            name='carrier',
            field=models.ForeignKey(to='travel.ServiceProvider', related_name='legs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leg',
            name='destination',
            field=models.ForeignKey(to='travel.Stop', related_name='outbound_legs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leg',
            name='origin',
            field=models.ForeignKey(to='travel.Stop', related_name='inbound_legs'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='leg',
            name='trip',
            field=models.ForeignKey(to='travel.Trip', related_name='legs'),
            preserve_default=True,
        ),
    ]
