# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_leg_year_in_school'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leg',
            old_name='year_in_school',
            new_name='type',
        ),
    ]
