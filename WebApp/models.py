from django.db import models

# Create your models here.
class Team(models.Model):
    tname=models.CharField(max_length=100)
    logourl=models.ImageField('media/',blank=True,null=True)
    state=models.CharField(max_length=100)

    def __str__(self):
        return  self.tname

class Player(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    player_image=models.ImageField('media/',blank=True,null=True)
    jersy_number=models.IntegerField()
    team=models.ForeignKey(Team,on_delete=models.CASCADE,)
    country=models.CharField(max_length=100)
    matches=models.IntegerField()
    runs=models.IntegerField()
    heightruns=models.IntegerField()
    half_centuries=models.IntegerField()
    centuries=models.IntegerField()

    def __str__(self):
        return  self.first_name

class Matches(models.Model):
    match_id=models.IntegerField()
    date=models.DateField()
    time=models.TimeField()
    team1=models.ForeignKey(Team,on_delete=models.CASCADE,related_name="team_one")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="team_two")
    result=models.ForeignKey(Team,on_delete=models.CASCADE,blank=True,null=True)

class Statistics(models.Model):
    team=models.ForeignKey(Team,on_delete=models.CASCADE,)
    playing_matches=models.IntegerField(default=0)
    win=models.IntegerField(default=0)
    loss=models.IntegerField(default=0)
    points=models.IntegerField(default=0)

    def __str__(self):
       return str(self.team)