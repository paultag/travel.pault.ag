# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0011_lodging_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserHome',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('place', models.ForeignKey(to='travel.Place', related_name='homes')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='home')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
