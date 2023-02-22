# Generated by Django 4.1.2 on 2023-02-22 06:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('culture_model', '0003_rename_index_vegetationindex'),
        ('gip', '0019_alter_contouryear_contour_alter_contouryear_type'),
        ('indexes', '0020_historicalscihubimagedate_polygon_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='IndexCreatingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_processed', models.BooleanField(default=False)),
                ('process_error', models.TextField()),
                ('contour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gip.contouryear')),
                ('satellite_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indexes.satelliteimages')),
                ('veg_index', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='culture_model.vegetationindex')),
            ],
        ),
    ]
