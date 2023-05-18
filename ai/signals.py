from decouple import config
from django.contrib.gis.db.models.functions import Area
from django.db import connection
from django.db.models.signals import post_save
from django.dispatch import receiver
from shapely.wkt import loads
import requests
from django.contrib.gis.geos import Point
from gip.models import Elevation
from ai.models.predicted_contour import Contour_AI
from ai.models.create_dataset import *
from threading import Thread
from ai.utils.predicted_contour import create_rgb, cut_rgb_tif, merge_bands, yolo
from ai.utils.create_dataset import create_dataset
import xarray as xr


@receiver(post_save, sender=Contour_AI)
def update(sender, instance, created, **kwargs):
    if created:
        geom = Contour_AI.objects.annotate(area_=Area("polygon")).get(id=instance.id)
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT subquery.name, subquery.id, subquery.soil_id, subquery.percent
                FROM (
                    SELECT ST_Area(ST_Intersection(scm.polygon::geometry,
                    '{geom.polygon}'::geography::geometry)) / ST_Area(scm.polygon::geometry) * 100 as percent,
                    sc.id, sc.name, scm.id as soil_id
                    FROM gip_soilclassmap as scm
                    JOIN gip_soilclass as sc
                    ON sc.id = scm.soil_class_id
                ) as subquery
                ORDER BY subquery.percent DESC
                LIMIT 1;
                     """)
            rows = cursor.fetchall()
            result_soil_class = rows[0][1] if rows != [] else None
        instance.soil_class_id = result_soil_class
        center = loads(f"{geom.polygon.centroid}".strip('SRID=4326;'))
        x, y = center.x, center.y
        data = xr.open_dataset(config('ELEVATION'))
        closest_point = data.sel(lat=y, lon=x, method='nearest')
        elevation = closest_point.elevation.values
        ha = round(geom.area_.sq_km * 100, 2)
        instance.elevation = elevation
        instance.area_ha = ha
        instance.save()
    else:
        geom = Contour_AI.objects.annotate(area_=Area("polygon")).get(id=instance.id)
        with connection.cursor() as cursor:
            cursor.execute(f"""
                SELECT subquery.name, subquery.id, subquery.soil_id, subquery.percent
                FROM (
                    SELECT ST_Area(ST_Intersection(scm.polygon::geometry,
                    '{geom.polygon}'::geography::geometry)) / ST_Area(scm.polygon::geometry) * 100 as percent,
                    sc.id, sc.name, scm.id as soil_id
                    FROM gip_soilclassmap as scm
                    JOIN gip_soilclass as sc
                    ON sc.id = scm.soil_class_id
                ) as subquery
                ORDER BY subquery.percent DESC
                LIMIT 1;
                     """)
            rows = cursor.fetchall()
            result_soil_class = rows[0][1] if rows != [] else None
        center = loads(f"{geom.polygon.centroid}".strip('SRID=4326;'))
        x, y = center.x, center.y
        data = xr.open_dataset(config('ELEVATION'))
        closest_point = data.sel(lat=y, lon=x, method='nearest')
        elevation = closest_point.elevation.values
        ha = round(geom.area_.sq_km * 100, 2)
        Contour_AI.objects.filter(id=instance.id).update(area_ha=ha, soil_class_id=result_soil_class,
                                                         elevation=elevation)


@receiver(post_save, sender=Process)
def merge_bands_handler(sender, instance, created, **kwargs):
    if created:
        thread_obj = Thread(target=merge_bands, args=(instance,))
        thread_obj.start()


@receiver(post_save, sender=Merge_Bands)
def create_RGB_handler(sender, instance, created, **kwargs):
    if created:
        thread_obj = Thread(target=create_rgb, args=(instance,))
        thread_obj.start()


@receiver(post_save, sender=Create_RGB)
def cut_RGB_TIF_handler(sender, instance, created, **kwargs):
    if created:
        thread_obj = Thread(target=cut_rgb_tif, args=(instance,))
        thread_obj.start()


@receiver(post_save, sender=Cut_RGB_TIF)
def choice_handler(sender, instance, created, **kwargs):
    if created:
        match instance.type_of_process:
            case 1:
                yolo()
            case 2:
                create_dataset()
