from django.contrib import admin
from django.contrib.gis import admin

from siasa.siasaapi.models import County
admin.site.register(County,admin.OSMGeoAdmin)
