from importlib.abc import MetaPathFinder
from tabnanny import verbose
from django.db import models


# Create your models here.
class Searched_data(models.Model):
    ip  =  models.GenericIPAddressField(null=True)
    continent = models.CharField(max_length=200, null=True)
    country = models.CharField(max_length=200, null=True)
    country_code = models.CharField(max_length=20, null=True)
    region   = models.CharField(max_length=200, null=True)
    region_code = models.CharField(max_length=20, null=True)
    city = models.CharField(max_length=200, null=True)
    user = models.CharField(max_length=200, null=True)
    date = models.DateField(auto_now_add=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    
    class Meta:
        verbose_name_plural = "searched api info"
   



    def __str__(self):
        return self.country



class Chart_table(models.Model):
    label = models.CharField(max_length=200, null=True)
    data = models.IntegerField( null=True)
    user = models.CharField(max_length=200, null=True)
    lat = models.FloatField(default=0)
    lng = models.FloatField(default=0)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "chart_table"
