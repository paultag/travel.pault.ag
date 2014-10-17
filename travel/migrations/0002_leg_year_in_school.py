# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leg',
            name='year_in_school',
            field=models.CharField(max_length=16, default='air', choices=[('air', 'Airplane'), ('train', 'Train'), ('bus', 'Bus')]),
            preserve_default=False,
        ),
    ]
