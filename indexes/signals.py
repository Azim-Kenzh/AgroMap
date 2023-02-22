import time
from threading import Thread

from django.db.models.signals import post_save
from django.dispatch import receiver

from indexes.models.satelliteimage import SatelliteImages
from indexes.utils import creating_indexes


@receiver(post_save, sender=SatelliteImages)
def creating_index_signal(sender, instance, created, **kwargs):
    time.sleep(60)
    if created:
        thread_object = Thread(target=creating_indexes, args=(instance.date, instance))
        thread_object.start()
