from django.conf.urls import patterns, include, url
from tastypie.resources import ModelResource
from tastypie.serializers import Serializer
from tastypie.authentication import ApiKeyAuthentication
from tastypie import fields


from siasa.siasaapi.models import Politician,Party,Education
from siasa.siasaapi.models import ElectionResults,Election,Constituency

class MPResource(ModelResource):
    constituency = fields.ForeignKey('siasa.siasaapi.api.ConstituencyResource','constituency',full=True)
    class Meta:
        queryset = Politician.objects.all()
        include_resource_uri = True
        resource_name= 'mp'

class PartyResource(ModelResource):
    mps = fields.ToManyField(MPResource,'politician_set',full=True)
    class Meta:
        queryset = Party.objects.all()
        include_resource_uri = True
        resource_name= 'parties'
        #authentication = ApiKeyAuthentication()

class EducationResource(ModelResource):
    class Meta:
        queryset = Education.objects.all()
        include_resource_uri = False
        resource_name= 'education'

class ResultsResource(ModelResource):
    class Meta:
        queryset = ElectionResults.objects.all()
        include_resource_uri = False
        resource_name= 'results'


class ElectionResource(ModelResource):
    #results = fields.ForeignKey(ResultsResource,'election',full=True)
    class Meta:
        queryset = Election.objects.all()
        include_resource_uri = False
        resource_name= 'elections'
    #def override_urls(self):
     #   return [
      #      url(r"^(?P<resource_name>%s)/(?P<year>[\w\d_.-]+)/$" % self._meta.resource_name, self.wrap_view('dispatch_detail'), name="api_dispatch_detail"),
       # ]
class ConstituencyResource(ModelResource):
    class Meta:
        queryset = Constituency.objects.all()
        include_resource_uri = True
        resource_name= 'constituencies'


class CandidaciesResource(ModelResource):
    party = fields.ToOneField(PartyResource, 'party',full=True)
    election = fields.ToOneField(ElectionResource,'election',full=True)
    constituency = fields.ForeignKey(ConstituencyResource,'constituency',full=True)
    class Meta:
        queryset = ElectionResults.objects.all()
        include_resource_uri = True
        resource_name= 'candidacies'

class PoliticianResource(ModelResource):
    party = fields.ToOneField(PartyResource, 'party',full=True)
    education = fields.ToManyField(EducationResource,'education_set',full=True)
    candidacies = fields.ToManyField(CandidaciesResource,'electionresults_set',full=True)
    class Meta:
        queryset = Politician.objects.all()
        include_resource_uri = True
        resource_name = 'politicians'
