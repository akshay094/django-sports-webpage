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
  userid = models.IntegerField()
  playerid = models.IntegerField()

  def __str__(self):
    return f"{self.userid} {self.playerid}"
      