from django.db import models
# Create your models here.
















class Task(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=1000)
    deadline = models.DateTimeField()
    myTeam = models.ForeignKey('Team', on_delete=models.CASCADE)
   # status = models.enums

    def __str__(self):
        return f'{self.title}\n {self.describe}'


class Team(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'
