from django.db import models

# Create your models here.
class Feature(models.Model):
    # id:int , automatically create a id IN db
    # name:str
    # details:str
    # is_true:bool , these without using DB
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)