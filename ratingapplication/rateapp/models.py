from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator


class MaxValudeValidator(object):
    pass


class Driver(models.Model):
    driver_id = models.PositiveIntegerField()
    driver_name = models.CharField(max_length=100)
    driver_rating = models.PositiveIntegerField()
    


class Meta:
    db_table = "Driver"

class Passenger(models.Model):
    passenger_id = models.PositiveIntegerField()
    passenger_name = models.CharField(max_length=100)
    passenger_rating = models.PositiveIntegerField()


class Meta:
    db_table = "Passenger"

