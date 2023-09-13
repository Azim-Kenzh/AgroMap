from django.urls import path, include

from gip.views.contact_information import DepartmentViewSet, ContactInformationViewSet
from gip.views.conton import ContonAPIView
from gip.views.contour import FilterContourAPIView, ContourStatisticsAPIView, StatisticsContourProductivityAPIView, \
    MapContourProductivityAPIView, CoordinatesPolygonAPIView, ContourSearchAPIView, AuthDetailContourViewSet, \
    CultureStatisticsAPIView
from gip.views.district import DistrictAPIView
from gip.views.polygon_and_point_in_polygon import OccurrenceCheckAPIView, PolygonsInBbox, PolygonsInScreen
from gip.views.region import RegionAPIView
from gip.views.soil import SoilAPIView, SoilClassAPIView
from gip.views.statistics import GraphicTablesAPIView, CulturePercentAPIView
from gip.views.culture import CultureViewSet
from gip.views.landtype import LandTypeAPIView
from gip.views.shapefile import UploadShapefileApiView, ExportShapefileApiView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('contour', AuthDetailContourViewSet)
router.register('culture', CultureViewSet)
router.register('department', DepartmentViewSet)
router.register('contact-information', ContactInformationViewSet)

urlpatterns = [
    path('soil-creating/', SoilAPIView.as_view()),
    path("occurrence-check/", OccurrenceCheckAPIView.as_view()),
    path("graphic-tables/", GraphicTablesAPIView.as_view()),
    path("culture-percent/", CulturePercentAPIView.as_view()),
    path("polygons-in-bbox/", PolygonsInBbox.as_view()),
    path('filter_contour/', FilterContourAPIView.as_view()),
    path('contour-statistics/', ContourStatisticsAPIView.as_view()),
    path('culture-statistics/', CultureStatisticsAPIView.as_view()),
    path('contour-statistics-productivity/', StatisticsContourProductivityAPIView.as_view()),
    path('contour-map-productivity/', MapContourProductivityAPIView.as_view()),
    path('coordinates-polygon/', CoordinatesPolygonAPIView.as_view()),
    path('contour-search/', ContourSearchAPIView.as_view()),
    path('polygons-in-screen/', PolygonsInScreen.as_view()),
    path('region/', RegionAPIView.as_view()),
    path('district/', DistrictAPIView.as_view()),
    path('conton/', ContonAPIView.as_view()),
    path('land-type/', LandTypeAPIView.as_view()),
    path('', include(router.urls)),
    path('soil-class/', SoilClassAPIView.as_view()),
    path("shapefile/upload/", UploadShapefileApiView.as_view(), name="shapefile-upload"),
    path("shapefile/export/", ExportShapefileApiView.as_view(), name="shapefile-export")
]
