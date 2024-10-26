from django.db import models

class Awards(models.Model):
    award_name = models.CharField(max_length=100)
    season = models.ForeignKey('Seasons', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'awards'


class Games(models.Model):
    game_date = models.DateField()
    location = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'games'


class Judges(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'judges'


class Matches(models.Model):
    game = models.ForeignKey(Games, models.DO_NOTHING)
    team1 = models.ForeignKey('Teams', models.DO_NOTHING)
    team2 = models.ForeignKey('Teams', models.DO_NOTHING, related_name='mainmatch_team2_set')
    winner_team = models.ForeignKey('Teams', models.DO_NOTHING, related_name='mainmatch_winner_team_set')

    class Meta:
        managed = False
        db_table = 'matches'


class Participants(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    team = models.ForeignKey('Teams', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'participants'


class Results(models.Model):
    score = models.IntegerField()
    game = models.ForeignKey(Games, models.DO_NOTHING)
    team = models.ForeignKey('Teams', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'results'


class Scores(models.Model):
    score = models.IntegerField()
    game = models.ForeignKey(Games, models.DO_NOTHING)
    judge = models.ForeignKey(Judges, models.DO_NOTHING)
    team = models.ForeignKey('Teams', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'scores'


class Seasons(models.Model):
    year = models.IntegerField()
    champion_team = models.ForeignKey('Teams', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'seasons'


class Teams(models.Model):
    team_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    year_formed = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'teams'


class Teamhistory(models.Model):
    event_date = models.DateField()
    event_description = models.TextField()
    team = models.ForeignKey(Teams, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_history'


class Teamstatistics(models.Model):
    total_games = models.IntegerField()
    total_wins = models.IntegerField()
    total_losses = models.IntegerField()
    team = models.ForeignKey(Teams, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'team_statistics'