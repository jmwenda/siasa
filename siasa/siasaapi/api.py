from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from siasa.siasaapi.models import Politician,Party

class PoliticianResource(ModelResource):
    class Meta:
        queryset = Politician.objects.all()
        include_resource_uri = True
        resource_name = 'politicians'

class PartyResource(ModelResource):
    class Meta:
        queryset = Party.objects.all()
        include_resource_uri = True
        resource_name= 'parties'

