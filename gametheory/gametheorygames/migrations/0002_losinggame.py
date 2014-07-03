# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gametheorygames', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LosingGame',
            fields=[
                ('depositAddress', models.TextField(default='')),
                ('game_ptr', models.OneToOneField(serialize=False, to='gametheorygames.Game', to_field='id', auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=('gametheorygames.game',),
        ),
    ]
