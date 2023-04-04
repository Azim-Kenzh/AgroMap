# Generated by Django 4.1.2 on 2023-04-04 09:34

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0049_remove_culture_fill_color_and_more'),
        ('ai', '0004_productivityml'),
    ]

    operations = [
        migrations.AddField(
            model_name='contour_ai',
            name='area_ha',
            field=models.FloatField(blank=True, null=True, verbose_name='Площадь в гектарах'),
        ),
        migrations.AddField(
            model_name='contour_ai',
            name='elevation',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Высота'),
        ),
        migrations.AddField(
            model_name='contour_ai',
            name='is_deleted',
            field=models.BooleanField(default=False, verbose_name='Удаленный'),
        ),
        migrations.AddField(
            model_name='contour_ai',
            name='soil_class',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='gip.soilclass', verbose_name='Тип почвы'),
        ),
        migrations.AddField(
            model_name='contour_ai',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ai_contours', to='gip.landtype', verbose_name='Тип земли'),
        ),
        migrations.AddField(
            model_name='contour_ai',
            name='year',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Год'),
        ),
        migrations.AlterField(
            model_name='contour_ai',
            name='conton',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contour_ai', to='gip.conton', verbose_name='Округ'),
        ),
        migrations.AlterField(
            model_name='contour_ai',
            name='polygon',
            field=django.contrib.gis.db.models.fields.GeometryField(blank=True, geography='Kyrgyzstan', null=True, srid=4326, verbose_name='Контур'),
        ),
        migrations.AlterField(
            model_name='contour_ai',
            name='productivity',
            field=models.CharField(blank=True, max_length=20, verbose_name='Продуктивность'),
        ),
    ]
