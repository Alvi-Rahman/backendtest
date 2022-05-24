from django.db import models


class Currency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=8)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=8)
    currencies = models.ManyToManyField(Currency)

    def __str__(self):
        return self.name
