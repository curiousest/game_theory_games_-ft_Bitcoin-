# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gametheorygames', '0002_losinggame'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='state',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
