from django.db import models
from django.contrib.gis.db import models
from django.contrib.auth.models import User
from tastypie.models import create_api_key

models.signals.post_save.connect(create_api_key, sender=User)

# Create your models here.
class County(models.Model):
    county = models.CharField("County",max_length=120)
    geom = models.MultiPolygonField()

    objects = models.GeoManager()

    def __unicode__(self):
        return self.county

    class Meta:
        verbose_name_plural = "Counties"

class Constituency(models.Model):
    constituency = models.CharField("Constituency",max_length=120)
    county =  models.ForeignKey(County)
    population = models.CharField(max_length=20)
    registeredvoters = models.CharField("Registered Voters",max_length=120)
    year = models.CharField("Year",max_length=120)
    def __unicode__(self):
        return self.constituency

class Election(models.Model):
    election = models.CharField("Election",max_length=120)
    year = models.CharField("Year",max_length=120)
    def __unicode__(self):
        return self.election

class Party(models.Model):
   party = models.CharField("Party Name",max_length=120)
   year_formed = models.DateTimeField()
   def __unicode__(self):
        return party

class Politician(models.Model):
   surname = models.CharField("Surname",max_length=120)
   othernames = models.CharField("Other Names", max_length=120)
   dateofbirth = models.DateTimeField("Date of Birth")
   brief = models.TextField("Brief")

