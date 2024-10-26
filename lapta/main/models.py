from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    year_formed = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'teams'


class Participants(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True, blank=True)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)

    class Meta:
        db_table = 'participants'


class Games(models.Model):
    game_date = models.DateField()
    location = models.CharField(max_length=100)

    class Meta:
        db_table = 'games'


class Results(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = 'results'


class Judges(models.Model):
    name = models.CharField(max_length=100)
    experience_years = models.IntegerField()

    class Meta:
        db_table = 'judges'


class Scores(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    judge = models.ForeignKey(Judges, on_delete=models.CASCADE)
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    score = models.IntegerField()

    class Meta:
        db_table = 'scores'


class Seasons(models.Model):
    year = models.IntegerField()
    champion_team = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'seasons'


class Awards(models.Model):
    award_name = models.CharField(max_length=100)
    season = models.ForeignKey(Seasons, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'awards'


class Matches(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE)
    team1 = models.ForeignKey(Teams, related_name='team1', on_delete=models.CASCADE)
    team2 = models.ForeignKey(Teams, related_name='team2', on_delete=models.CASCADE)
    winner_team = models.ForeignKey(Teams, related_name='winner_team', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'matches'


class TeamStatistics(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    total_games = models.IntegerField(default=0)
    total_wins = models.IntegerField(default=0)
    total_losses = models.IntegerField(default=0)

    class Meta:
        db_table = 'team_statistics'


class TeamHistory(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE)
    event_date = models.DateField()
    event_description = models.TextField()

    class Meta:
        db_table = 'team_history'
