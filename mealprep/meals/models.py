from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Foods(models.Model):
    # fid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
    volume = models.IntegerField()
    calories = models.IntegerField(null=True)
    protein = models.IntegerField(null=True)

    def __str__(self):
        return self.name

class User_Fridge(models.Model):
    uid = models.ForeignKey(User, on_delete=models.CASCADE)
    fid = models.ForeignKey(Foods, on_delete=models.CASCADE, unique=True)
    volume = models.IntegerField()

    def __str__(self):
        return str(self.uid) + ', ' + str(self.fid)
    
    class Meta:
        unique_together = ('uid', 'fid')

class Recipes(models.Model):
    # fid = models.AutoField(primary_key=True)()
    name = models.CharField(max_length=1024)
    directions = models.CharField(max_length=1024)
    ingridients = models.CharField(max_length=1024)
    type = models.CharField(max_length=16)
    time = models.IntegerField(null=True)
    image = models.CharField(max_length=256, null=True)

    def __str__(self):
        return models.name


