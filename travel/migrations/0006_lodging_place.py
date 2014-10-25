# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_lodging_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodging',
            name='place',
            field=models.ForeignKey(to='travel.Place', default=1, related_name='lodgings'),
            preserve_default=False,
        ),
    ]
