# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Color(models.Model):
    color_id = models.AutoField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'color'


class Player(models.Model):
    player_id = models.AutoField(primary_key=True)
    team_id = models.IntegerField(blank=True, null=True)
    uniform_num = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=40, blank=True, null=True)
    last_name = models.CharField(max_length=40, blank=True, null=True)
    mpg = models.IntegerField(blank=True, null=True)
    ppg = models.IntegerField(blank=True, null=True)
    rpg = models.IntegerField(blank=True, null=True)
    apg = models.IntegerField(blank=True, null=True)
    spg = models.DecimalField(max_digits=18, decimal_places=1, blank=True, null=True)
    bpg = models.DecimalField(max_digits=18, decimal_places=1, blank=True, null=True)

    def __str__(self):
        return str(self.player_id)

    class Meta:
        managed = False
        db_table = 'player'


class State(models.Model):
    state_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2, blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'state'

class Team(models.Model):
    team_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True, null=True)
    state_id = models.IntegerField(blank=True, null=True)
    color_id = models.IntegerField(blank=True, null=True)
    wins = models.IntegerField(blank=True, null=True)
    losses = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        managed = False
        db_table = 'team'
