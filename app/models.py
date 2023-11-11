from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Card(models.Model):
    url = models.URLField()

class Field(models.Model):
    difficulty = models.CharField(max_length=255)
    layout = models.JSONField()
    history = models.JSONField()
    players = models.JSONField()
    current_player = models.CharField(max_length=255)
