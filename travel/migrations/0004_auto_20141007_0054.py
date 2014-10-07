# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20141007_0039'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('code', models.CharField(max_length=16)),
                ('lat', models.CharField(max_length=128)),
                ('lon', models.CharField(max_length=128)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='flight',
            name='destination',
            field=models.ForeignKey(default=None, related_name='outbound_flights', to='travel.Airport'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='flight',
            name='origin',
            field=models.ForeignKey(default=None, related_name='inbound_flights', to='travel.Airport'),
            preserve_default=False,
        ),
    ]
