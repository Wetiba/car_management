# cars/models.py
from django.db import models

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    mileage = models.PositiveIntegerField()
    color = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.make} {self.model} ({self.year})"

class VehicleLocation(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

class DropOff(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    location = models.ForeignKey(VehicleLocation, on_delete=models.CASCADE)
    drop_off_time = models.DateTimeField(auto_now_add=True)

