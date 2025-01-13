# models.py
from django.db import models

class BuildingEnergyData(models.Model):
    building_name = models.CharField(max_length=50)
    date = models.DateField()
    energy_consumption = models.FloatField()

    def __str__(self):
        return f"{self.building_name} - {self.date}"
