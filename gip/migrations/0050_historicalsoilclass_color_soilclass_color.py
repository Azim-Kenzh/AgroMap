# Generated by Django 4.1.2 on 2023-04-20 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gip', '0049_remove_culture_fill_color_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='historicalsoilclass',
            name='color',
            field=models.CharField(max_length=20, null=True, verbose_name='Цвет'),
        ),
        migrations.AddField(
            model_name='soilclass',
            name='color',
            field=models.CharField(max_length=20, null=True, verbose_name='Цвет'),
        ),
    ]
