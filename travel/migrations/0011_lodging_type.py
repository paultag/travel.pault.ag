# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0010_stay_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='lodging',
            name='type',
            field=models.CharField(max_length=16, default='hotel', choices=[('hotel', 'Hotel'), ('house', 'House')]),
            preserve_default=False,
        ),
    ]
