from django.db import models
from django.utils import timezone


class Brand(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    website = models.URLField()
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    name = models.CharField(max_length=200)
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.name


class PurchasedAd(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    package = models.CharField(max_length=350)
    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    cost = models.IntegerField()
    objective = models.TextField()
    ad_date = models.DateField()
    created_on = models.DateTimeField(default=timezone.now())

    def __str__(self):
        string = "{} - {}".format(self.brand, self.objective)
        return string
