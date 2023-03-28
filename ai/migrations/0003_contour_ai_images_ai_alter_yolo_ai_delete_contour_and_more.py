# Generated by Django 4.1.2 on 2023-03-28 07:11

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0048_alter_district_polygon_and_more'),
        ('ai', '0002_remove_contour_canton_remove_contour_conf_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contour_AI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('polygon', django.contrib.gis.db.models.fields.GeometryField(blank=True, geography='Kyrgyzstan', null=True, srid=4326)),
                ('percent', models.FloatField(blank=True, null=True)),
                ('culture', models.CharField(blank=True, max_length=50, null=True)),
                ('productivity', models.CharField(blank=True, max_length=20)),
                ('conton', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contour_ai', to='gip.conton')),
                ('district', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contour_ai', to='gip.district')),
            ],
        ),
        migrations.CreateModel(
            name='Images_AI',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images_ai')),
            ],
        ),
        migrations.AlterField(
            model_name='yolo',
            name='ai',
            field=models.FileField(upload_to='models_ai/'),
        ),
        migrations.DeleteModel(
            name='Contour',
        ),
        migrations.DeleteModel(
            name='Images',
        ),
        migrations.AddField(
            model_name='contour_ai',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='contour_ai', to='ai.images_ai'),
        ),
    ]
