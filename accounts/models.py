from django.db import models
from django.contrib.auth.models import User


# Create your models here


class Farmer(models.Model):
    farmer=models.AutoField(primary_key=True)
    farmer_name=models.CharField(max_length=50)

    def __str__(self):
        return self.farmer_name

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE, null=True)
    useat = models.CharField(max_length=100)
    
    @property
    def useat_as_list(self):
        return self.useat.split(',')
    def __str__(self):
        return self.farmer.farmer_name

