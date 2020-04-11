from django.db import models

class Earthquake(models.Model):
    date = models.DateField()
    latitude = models.DecimalField(max_digits=10, decimal_places=5)
    longitude = models.DecimalField(max_digits=10, decimal_places=5)
    depth = models.DecimalField(max_digits=10, decimal_places=5)
    magnitude = models.DecimalField(max_digits=10, decimal_places=5)

    def __str__(self):
        return self.date
