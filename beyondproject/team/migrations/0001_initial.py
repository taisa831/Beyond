# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamAdminUsers',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('user_name', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('del_flg', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'team_admin_users',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamGameFirstHalfScores',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('score', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'team_game_first_half_scores',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamGameInnings',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('inning', models.IntegerField()),
                ('del_flg', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'team_game_innings',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamGamePlayers',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('stolen_base_count', models.IntegerField()),
                ('del_flg', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'team_game_players',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamGamePlayerScores',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('status', models.IntegerField()),
                ('out_flg', models.IntegerField()),
                ('del_flg', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'team_game_player_scores',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamGames',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('game_date', models.DateTimeField()),
                ('first_half_team_name', models.CharField(max_length=255)),
                ('second_half_team_name', models.CharField(max_length=255)),
                ('del_flg', models.IntegerField()),
                ('created_at', models.CharField(max_length=255)),
                ('updated_at', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'team_games',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamGameSecondHalfScores',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('score', models.IntegerField()),
                ('del_flg', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'team_game_second_half_scores',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='TeamPlayers',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('player_name', models.CharField(max_length=45)),
                ('del_flg', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'team_players',
                'managed': False,
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teams',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('team_name', models.CharField(max_length=254)),
                ('del_flg', models.IntegerField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
            options={
                'db_table': 'teams',
                'managed': False,
            },
            bases=(models.Model,),
        ),
    ]
