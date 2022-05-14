from django.db import models

# Create your models here.

class Foods(models.Model):
    fid = models.PrimaryKey()
    name = models.CharField(max_length=256)
    volume = models.IntegerField()
    calories = models.IntegerField()
    protein = models.IntegerField()

class User_Fridge(models.Model):
    uid = models.PrimaryKey()
    fid = models.ForeignKey(Foods, on_delete=models.CASCADE)
    volume = models.IntegerField()

class Recipes(models.Model):
    fid = models.PrimaryKey()
    name = models.CharField(1024)
    directions = models.CharField(1024)
    ingridients = models.CharField(1024)
    type = models.CharField(16)
    time = models.IntegerField()
    image = models.CharField(256)


