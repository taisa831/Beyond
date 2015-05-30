from django.db import models

class BaseballTeamAdminUsers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team = models.ForeignKey('BaseballTeams')
    admin_user_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'baseball_team_admin_users'


class BaseballTeamGameBottomScores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_game = models.ForeignKey('BaseballTeamGames')
    inning = models.IntegerField()
    score = models.IntegerField()
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'baseball_team_game_bottom_scores'


class BaseballTeamGameTopScores(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team_game = models.ForeignKey('BaseballTeamGames')
    inning = models.IntegerField()
    score = models.IntegerField()
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'baseball_team_game_top_scores'


class BaseballTeamGames(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team = models.ForeignKey('BaseballTeams')
    game_date = models.DateTimeField()
    top_team_name = models.CharField(max_length=255)
    bottom_team_name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'baseball_team_games'


class BaseballTeamPlayers(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    team = models.ForeignKey('BaseballTeams')
    player_name = models.CharField(max_length=45)
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'baseball_team_players'


class BaseballTeams(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(max_length=254)
    del_flg = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'baseball_teams'
