# Generated by Django 4.1.2 on 2023-03-28 07:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0047_contour_soil_class_historicalcontour_soil_class'),
        ('ai', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contour',
            name='canton',
        ),
        migrations.RemoveField(
            model_name='contour',
            name='conf',
        ),
        migrations.AddField(
            model_name='contour',
            name='conton',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='canton', to='gip.conton'),
        ),
        migrations.AddField(
            model_name='contour',
            name='district',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, related_name='district', to='gip.district'),
        ),
        migrations.AddField(
            model_name='contour',
            name='percent',
            field=models.FloatField(default=0.5, null=True),
        ),
        migrations.DeleteModel(
            name='Canton',
        ),
    ]
