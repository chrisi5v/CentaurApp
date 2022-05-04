from django.db import models
from django.contrib.auth.models import AbstractUser


class Vehicle(models.Model):
    name = models.CharField(max_length = 30)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.name

class User(AbstractUser):
    DRIVER = 'DR'
    SUPERVISOR = 'SP'
    role = models.CharField(
        max_length=2,
        choices=[
            (DRIVER, 'Driver'),
            (SUPERVISOR, 'Supervisor'),
         ],
        default=DRIVER,
    )
    vehicle =  models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True)

class VehicleChecklist(models.Model):
    vehicle =  models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    driver = models.ForeignKey(User, on_delete=models.CASCADE)
    brakes = models.BooleanField(null=False, default=False)
    wipers = models.BooleanField(null=False, default=False)
    tires = models.BooleanField(null=False, default=False)
    oil = models.BooleanField(null=False, default=False)
    gas = models.BooleanField(null=False, default=False)
    seatbelt = models.BooleanField(null=False, default=False)
    comment = models.TextField(null=True, blank = True)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True) 

    class  Meta:
        ordering = ['-created']

    def __str__(self):
        return str(self.created)

