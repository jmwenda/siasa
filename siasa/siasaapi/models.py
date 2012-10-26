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

ELECTION_TYPE = (('1','General'),('2','By-election'),('3','Other'))
class Election(models.Model):
    election = models.CharField("Election",max_length=120)
    election_type = models.CharField(max_length=25,choices=ELECTION_TYPE)
    year = models.CharField("Year",max_length=120)
    def __unicode__(self):
        return self.election

class Party(models.Model):
   party = models.CharField("Party Name",max_length=120)
   year_formed = models.DateTimeField()
   def __unicode__(self):
        return self.party

class Politician(models.Model):
   surname = models.CharField("Surname",max_length=120)
   othernames = models.CharField("Other Names", max_length=120)
   dateofbirth = models.DateTimeField("Date of Birth")
   brief = models.TextField("Brief")
   party = models.ForeignKey(Party)
   twitter = models.CharField("Twitter",max_length=120)
   facebook = models.CharField("FaceBook",max_length=150)
   telephone = models.CharField("Phone",max_length=150)
   email = models.CharField("Email",max_length=150)
   is_incumbent = models.BooleanField(default=True)
   constituency = models.ForeignKey(Constituency)
   def __unicode__(self):
        return str('%s %s' % (self.surname, self.othernames))


EDU_TYPE = (('Doctorate','1'),('Masters','2'),('Graduate','3'))

class Education(models.Model):
   education_type = models.CharField(max_length=25,choices=EDU_TYPE)
   university = models.CharField(max_length=50)
   politician = models.ForeignKey(Politician)


class ElectionResults(models.Model):
   election = models.ForeignKey(Election)
   constituency = models.ForeignKey(Constituency)
   politician = models.ForeignKey(Politician)
   party = models.ForeignKey(Party)
   votes = models.FloatField("Votes",max_length=25)
   winner = models.BooleanField("Won",default=True)
   def __unicode__(self):
        return str('%s %s' % (self.election, self.constituency))


