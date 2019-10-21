from django.db import models

# Create your models here.
class Substation(models.Model):
    name = models.CharField(max_length=200)
    lattitude = models.DecimalField(max_digits=20, decimal_places=15)
    longtitude = models.DecimalField(max_digits=20, decimal_places=15)
    capacity = models.DecimalField(max_digits=20, decimal_places=15)

    def __str__(self):
        return self.name
