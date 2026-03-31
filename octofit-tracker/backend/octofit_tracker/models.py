
from django.db import models
from django.contrib.auth.models import AbstractUser
from bson import ObjectId

class Team(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100, unique=True)

class User(AbstractUser):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    email = models.EmailField(unique=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True)

class Activity(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=50)
    duration = models.IntegerField()

class Workout(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()

class Leaderboard(models.Model):
    id = models.CharField(primary_key=True, max_length=24, default=lambda: str(ObjectId()), editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
