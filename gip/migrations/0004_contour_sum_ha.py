# Generated by Django 4.1.2 on 2022-11-24 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0003_alter_conton_polygon_alter_district_polygon_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contour',
            name='sum_ha',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
