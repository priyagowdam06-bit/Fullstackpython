from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()

class Reservation(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    gust_count = models.IntegerField()
    Reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=10000)