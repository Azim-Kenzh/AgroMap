# Generated by Django 4.1.2 on 2023-02-15 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hub', '0002_historicallandinfo_ate2_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallandinfo',
            name='ink_code',
            field=models.CharField(max_length=100, verbose_name='Код ИНК'),
        ),
        migrations.AlterField(
            model_name='landinfo',
            name='ink_code',
            field=models.CharField(max_length=100, verbose_name='Код ИНК'),
        ),
    ]
