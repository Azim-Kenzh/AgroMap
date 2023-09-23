from django.contrib.gis.db import models
from django.utils.translation import gettext_lazy as _


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name=_('Creation Date'))
    updated_at = models.DateTimeField(auto_now=True, verbose_name=_("Update Date"))

    class Meta:
        abstract = True

