from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Card(models.Model):
    number = models.IntegerField()
    url = models.URLField()

class Field(models.Model):
    size = models.IntegerField()
    difficulty = models.CharField(max_length=255)
    layout = models.JSONField()
