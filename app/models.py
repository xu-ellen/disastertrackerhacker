from django.db import models

class Earthquake(models.Model):
    date = models.DateField()
    latitude = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)
    depth = models.DecimalField(max_digits=10, decimal_places=5)
    magnitude = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return str(self.date)


class ForestFire(models.Model):
    name = models.CharField(max_length=50)
    year = models.CharField(max_length=10)
    latitude = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)
    size = models.DecimalField(max_digits=5, decimal_places=3)
    size_class = models.CharField(max_length=1)
    
    def __str__(self):
        return self.name
