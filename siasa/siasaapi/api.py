from tastypie.resources import ModelResource
from tastypie.serializers import Serializer

from siasa.siasaapi.models import Politician

class PoliticianResource(ModelResource):
    class Meta:
        queryset = Politician.objects.all()
        include_resource_uri = True
        resource_name = 'politician'

