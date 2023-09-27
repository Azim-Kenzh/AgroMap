# Generated by Django 4.1.2 on 2023-09-27 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0065_alter_conton_options_alter_historicalconton_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contour',
            name='predicted_productivity',
            field=models.CharField(blank=True, default='1.0', max_length=20, null=True, verbose_name='Predicted Productivity'),
        ),
        migrations.AlterField(
            model_name='contour',
            name='productivity',
            field=models.CharField(blank=True, default='1.0', max_length=20, null=True, verbose_name='Productivity'),
        ),
        migrations.AlterField(
            model_name='historicalcontour',
            name='predicted_productivity',
            field=models.CharField(blank=True, default='1.0', max_length=20, null=True, verbose_name='Predicted Productivity'),
        ),
        migrations.AlterField(
            model_name='historicalcontour',
            name='productivity',
            field=models.CharField(blank=True, default='1.0', max_length=20, null=True, verbose_name='Productivity'),
        ),
    ]
