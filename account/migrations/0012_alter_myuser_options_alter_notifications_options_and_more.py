# Generated by Django 4.1.2 on 2023-09-23 07:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_myuser_options_alter_notifications_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='myuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'Users'},
        ),
        migrations.AlterModelOptions(
            name='notifications',
            options={'verbose_name': 'Notification', 'verbose_name_plural': 'Notifications'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Profile', 'verbose_name_plural': 'Profiles'},
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_employee',
            field=models.BooleanField(default=False, verbose_name='Worker'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_farmer',
            field=models.BooleanField(default=False, verbose_name='Farmer'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name='Administrator'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_supervisor',
            field=models.BooleanField(default=False, verbose_name='Observer'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='date',
            field=models.DateTimeField(auto_now=True, verbose_name='Created date'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='is_read',
            field=models.BooleanField(default=False, verbose_name='Read'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='text',
            field=models.CharField(max_length=100, verbose_name='Notification text'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='text_en',
            field=models.CharField(max_length=100, null=True, verbose_name='Notification text'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='text_ky',
            field=models.CharField(max_length=100, null=True, verbose_name='Notification text'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='text_ru',
            field=models.CharField(max_length=100, null=True, verbose_name='Notification text'),
        ),
        migrations.AlterField(
            model_name='notifications',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification', to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(max_length=55, verbose_name='Full name'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='my_user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='profiles', serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=14, verbose_name='Phone number'),
        ),
    ]
