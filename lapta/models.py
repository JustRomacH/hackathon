# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    first_name = models.CharField(max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

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
    team = models.ForeignKey("Teams", models.DO_NOTHING)

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