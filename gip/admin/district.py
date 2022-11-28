from django.contrib.gis import admin
from simple_history.admin import SimpleHistoryAdmin

from gip.models import District
from leaflet.admin import LeafletGeoAdmin


@admin.register(District)
class DistrictAdmin(LeafletGeoAdmin, SimpleHistoryAdmin):
    list_display = ['id', 'name', 'region']
    readonly_fields = ('id', 'created_at', 'updated_at')
    list_filter = ('region', 'name', )
    ordering = ('name', 'created_at')
    list_per_page = 20
    search_fields = ('name', 'region')
    date_hierarchy = 'created_at'
    list_display_links = ('id', 'name', )

