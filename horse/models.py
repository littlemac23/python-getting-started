from django.db import models
from django.conf import settings
from django.contrib.auth.models import User



class Horse(models.Model):
    name = models.CharField(max_length = 120)
    acquisitionDate = models.DateField()
    totalAcquisitionAmount = models.IntegerField()
    type = models.CharField(max_length = 120)
    place = models.CharField(max_length = 120)
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True)
    sold = models.BooleanField(default=False)
    sellingPrice = models.IntegerField(default=0)

    def __str__(self):
        return str(self.name)

class Race(models.Model):
    earning = models.IntegerField()
    month = models.CharField(max_length = 120)
    year = models.IntegerField()
    raceDate = models.DateField()
    finish = models.CharField(max_length = 120)
    type = models.CharField(max_length = 120)
    name = models.ForeignKey(Horse, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name) + ' ' + str(self.raceDate)

class Expense(models.Model):
    month = models.CharField(max_length = 120)
    year = models.CharField(max_length = 120)
    decription = models.CharField(max_length = 120)
    total = models.IntegerField()
    name = models.ForeignKey(Horse, on_delete = models.CASCADE)

    def __str__(self):
        return str(self.name)+ ' ' + str(self.decription) + ' ' + str(self.id)
