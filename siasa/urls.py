from django.conf.urls import patterns, include, url
from tastypie.api import Api
from siasa.siasaapi.api import PoliticianResource,PartyResource
from siasa.siasaapi.api import CandidaciesResource,EducationResource
from siasa.siasaapi.api import ConstituencyResource,MPResource
from siasa.siasaapi.api import ElectionResource,ResultsResource

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(PoliticianResource())
v1_api.register(PartyResource())
v1_api.register(EducationResource())
v1_api.register(CandidaciesResource())
v1_api.register(ConstituencyResource())
v1_api.register(MPResource())
v1_api.register(ElectionResource())
v1_api.register(ResultsResource())
#import pdb;pdb.set_trace()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'siasa.views.home', name='home'),
    # url(r'^siasa/', include('siasa.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(v1_api.urls)),
)
