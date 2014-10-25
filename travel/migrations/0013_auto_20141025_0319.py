# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0012_userhome'),
    ]

    operations = [
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('place', models.ForeignKey(to='travel.Place', related_name='homes')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='home')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='userhome',
            name='place',
        ),
        migrations.RemoveField(
            model_name='userhome',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserHome',
        ),
    ]
