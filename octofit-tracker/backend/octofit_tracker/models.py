from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

class Team(models.Model):
    name = models.CharField(max_length=100)

class Activity(models.Model):
    user = models.CharField(max_length=100)  # Store user reference as a string (e.g., username or email)
    activity_type = models.CharField(max_length=100)
    duration = models.DurationField()

class Leaderboard(models.Model):
    user = models.CharField(max_length=100)  # Store user reference as a string
    score = models.IntegerField()

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
