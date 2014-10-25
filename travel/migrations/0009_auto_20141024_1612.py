# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0008_lodging_time_zone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stay',
            old_name='checkin',
            new_name='checkin_time',
        ),
        migrations.RenameField(
            model_name='stay',
            old_name='checkout',
            new_name='checkout_time',
        ),
    ]
