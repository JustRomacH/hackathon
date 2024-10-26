from django.db import models


class Teams(models.Model):
    team_name = models.CharField(max_length=100, verbose_name="Название команды")
    city = models.CharField(max_length=100, verbose_name="Город")
    year_formed = models.IntegerField(null=True, blank=True, verbose_name="Год основания")

    class Meta:
        db_table = 'teams'

    def __str__(self):
        return f"{self.team_name} ({self.city})"


class Participants(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя участника")
    age = models.IntegerField(null=True, blank=True, verbose_name="Возраст")
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Команда")

    class Meta:
        db_table = 'participants'

    def __str__(self):
        return self.name

class Games(models.Model):
    game_date = models.DateField(verbose_name="Дата игры")
    location = models.CharField(max_length=100, verbose_name="Место проведения")

    class Meta:
        db_table = 'games'

    def __str__(self):
        return f"Игра от {self.game_date} в {self.location}"


class Results(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name="Игра")
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Команда")
    score = models.IntegerField(verbose_name="Счет")

    class Meta:
        db_table = 'results'

    def __str__(self):
        return f"{self.team} - {self.score} очков"


class Judges(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя судьи")
    experience_years = models.IntegerField(verbose_name="Годы опыта")

    class Meta:
        db_table = 'judges'

    def __str__(self):
        return self.name

class Scores(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name="Игра")
    judge = models.ForeignKey(Judges, on_delete=models.CASCADE, verbose_name="Судья")
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Команда")
    score = models.IntegerField(verbose_name="Оценка")

    class Meta:
        db_table = 'scores'

    def __str__(self):
        return f"Оценка {self.score} для {self.team} от {self.judge}"

class Seasons(models.Model):
    year = models.IntegerField(verbose_name="Год")
    champion_team = models.ForeignKey(Teams, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Чемпион")

    class Meta:
        db_table = 'seasons'

    def __str__(self):
        return f"Сезон {self.year}"

class Awards(models.Model):
    award_name = models.CharField(max_length=100, verbose_name="Название награды")
    season = models.ForeignKey(Seasons, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Сезон")

    class Meta:
        db_table = 'awards'

    def __str__(self):
        return f"{self.award_name} - {self.season}"

class Matches(models.Model):
    game = models.ForeignKey(Games, on_delete=models.CASCADE, verbose_name="Игра")
    team1 = models.ForeignKey(Teams, related_name='team1', on_delete=models.CASCADE, verbose_name="Команда 1")
    team2 = models.ForeignKey(Teams, related_name='team2', on_delete=models.CASCADE, verbose_name="Команда 2")
    winner_team = models.ForeignKey(Teams, related_name='winner_team', on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Победившая команда")

    class Meta:
        db_table = 'matches'

    def __str__(self):
        return f"Матч между {self.team1} и {self.team2} - Победитель: {self.winner_team}"

class TeamStatistics(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Команда")
    total_games = models.IntegerField(default=0, verbose_name="Всего игр")
    total_wins = models.IntegerField(default=0, verbose_name="Всего побед")
    total_losses = models.IntegerField(default=0, verbose_name="Всего поражений")

    class Meta:
        db_table = 'team_statistics'

    def __str__(self):
        return f"Статистика команды {self.team}"

class TeamHistory(models.Model):
    team = models.ForeignKey(Teams, on_delete=models.CASCADE, verbose_name="Команда")
    event_date = models.DateField(verbose_name="Дата события")
    event_description = models.TextField(verbose_name="Описание события")

    class Meta:
        db_table = 'team_history'

    def __str__(self):
        return f"История команды {self.team}: {self.event_date}"
