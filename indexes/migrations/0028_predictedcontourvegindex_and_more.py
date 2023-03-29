# Generated by Django 4.1.2 on 2023-03-29 11:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('culture_model', '0005_alter_decade_options_alter_indexplan_options_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ai', '0004_productivityml'),
        ('indexes', '0027_remove_satelliteimages_decade_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PredictedContourVegIndex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('index_image', models.FileField(blank=True, upload_to='index_image')),
                ('average_value', models.DecimalField(blank=True, decimal_places=3, max_digits=5)),
                ('date', models.DateField()),
                ('contour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contour_ai_veg_index', to='ai.contour_ai')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='culture_model.vegetationindex')),
                ('meaning_of_average_value', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indexes.indexmeaning')),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalPredictedContourVegIndex',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('index_image', models.TextField(blank=True, max_length=100)),
                ('average_value', models.DecimalField(blank=True, decimal_places=3, max_digits=5)),
                ('date', models.DateField()),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('contour', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='ai.contour_ai')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('index', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='culture_model.vegetationindex')),
                ('meaning_of_average_value', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='indexes.indexmeaning')),
            ],
            options={
                'verbose_name': 'historical predicted contour veg index',
                'verbose_name_plural': 'historical predicted contour veg indexs',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='ContourAIIndexCreatingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_processed', models.BooleanField(default=False)),
                ('process_error', models.TextField()),
                ('contour', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='ai.contour_ai')),
                ('satellite_image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='indexes.scihubimagedate')),
                ('veg_index', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='culture_model.vegetationindex')),
            ],
        ),
    ]
