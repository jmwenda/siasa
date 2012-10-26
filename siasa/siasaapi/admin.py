from django.contrib import admin
from django.contrib.gis import admin

from siasa.siasaapi.models import County,Politician,Party
from siasa.siasaapi.models import Education,Constituency
from siasa.siasaapi.models import Election,ElectionResults

class EducationInline(admin.TabularInline):
    model = Education
    #extra = 20
class CandidaciesInline(admin.TabularInline):
    model = ElectionResults
class PoliticianAdmin(admin.ModelAdmin):
    inlines = [EducationInline,CandidaciesInline]

admin.site.register(County,admin.OSMGeoAdmin)
admin.site.register(Politician,PoliticianAdmin)
admin.site.register(Education)
admin.site.register(Party)
admin.site.register(Constituency)
admin.site.register(Election)
admin.site.register(ElectionResults)
