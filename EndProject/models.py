from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return f'{self.name}'

class User(models.Model):
    username = models.EmailField(unique=True)
    password = models.CharField(max_length=20)
    role = models.CharField(max_length=20, choices=(('admin', 'Admin'), ('worker', 'Worker')), default='Worker')
    myTeam =  models.ForeignKey(Team, on_delete = models.DO_NOTHING, null = True, blank = True)
    def __str__(self):
        return self.username

class Task(models.Model):
    title = models.CharField(max_length=100)
    describe = models.CharField(max_length=1000)
    deadline = models.DateTimeField()
    status = models.CharField(max_length=20, choices=[('new', 'New'), ('process','Process'), ('done', 'Done')] , default='new')
    myTeam = models.ForeignKey(Team, on_delete=models.DO_NOTHING, null=True, blank=True)
    myDoner = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.title}\n {self.describe}'
