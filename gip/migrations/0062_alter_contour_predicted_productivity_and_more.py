# Generated by Django 4.1.2 on 2023-08-17 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0061_alter_contour_pasture_culture_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contour',
            name='predicted_productivity',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Прогнозируемая продуктивность'),
        ),
        migrations.AlterField(
            model_name='historicalcontour',
            name='predicted_productivity',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='Прогнозируемая продуктивность'),
        ),
    ]
