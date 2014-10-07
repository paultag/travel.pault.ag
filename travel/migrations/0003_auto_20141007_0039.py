# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_flight_flight_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='name',
            field=models.CharField(default=None, max_length=128),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='flight',
            name='carrier',
            field=models.ForeignKey(to='travel.ServiceProvider', related_name='flights'),
        ),
        migrations.AlterField(
            model_name='flight',
            name='flight_number',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='name',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='phone_number',
            field=models.CharField(max_length=32),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='rewards_account',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='serviceprovider',
            name='website',
            field=models.URLField(),
        ),
    ]
