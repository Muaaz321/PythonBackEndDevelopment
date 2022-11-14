from django.db import models
from datetime import datetime

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.CharField(max_length=1000000)
    created_at = models.DateField(default=datetime.now,blank=True)

    # we have to do the migration after creation of model
    # python manage.py makemigrations
    # python manage.py migrate
    # python manage.py createsuperuser << create DB user
