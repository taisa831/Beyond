from django.db import models

# Create your models here.
class TeamAdminUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team = models.ForeignKey('Teams')
    user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_admin_users'


class TeamGameFirstHalfScores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_game = models.ForeignKey('TeamGames')
    team_game_inning = models.ForeignKey('TeamGameInnings', db_column='team_game_inning')
    score = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_game_first_half_scores'


class TeamGameInnings(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_game = models.ForeignKey('TeamGames')
    inning = models.IntegerField()
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_game_innings'


class TeamGamePlayerScores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_game_inning = models.ForeignKey(TeamGameInnings)
    team_game_player = models.ForeignKey('TeamGamePlayers')
    status = models.IntegerField()
    out_flg = models.IntegerField()
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_game_player_scores'


class TeamGamePlayers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_game = models.ForeignKey('TeamGames')
    team_player = models.ForeignKey('TeamPlayers')
    stolen_base_count = models.IntegerField()
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_game_players'


class TeamGameSecondHalfScores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_game = models.ForeignKey('TeamGames')
    team_game_inning = models.ForeignKey(TeamGameInnings, db_column='team_game_inning')
    score = models.IntegerField()
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_game_second_half_scores'


class TeamGames(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team = models.ForeignKey('Teams')
    game_date = models.DateTimeField()
    first_half_team_name = models.CharField(max_length=255)
    second_half_team_name = models.CharField(max_length=255)
    del_flg = models.IntegerField()
    created_at = models.CharField(max_length=255)
    updated_at = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'team_games'


class TeamPlayers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team = models.ForeignKey('Teams')
    player_name = models.CharField(max_length=45)
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'team_players'


class Teams(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_name = models.CharField(max_length=254)
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'teams'