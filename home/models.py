from django.db import models
# Create your models here.

class players(models.Model):
  playerName = models.CharField(max_length=50)
  playerHeight = models.CharField(max_length=4)
  playerTeam = models.CharField(max_length=50)
  playerGoals = models.CharField(max_length=50)
  playerTotalMatches = models.CharField(max_length=50)
  playerImg = models.ImageField(upload_to='static/img', default="")

class team(models.Model):
  name = models.CharField(max_length=50)
  userid = models.IntegerField()
  playerid = models.IntegerField()