from django.db import models

# Create your models here.
class Movies(models.Model):
    moviename=models.CharField(max_length=100)
    ticketprice=models.IntegerField()