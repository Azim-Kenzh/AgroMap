# Generated by Django 4.1.4 on 2022-12-15 21:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("auditlog", "0012_add_logentry_action_access"),
    ]

    operations = [
        migrations.AlterField(
            model_name="logentry",
            name="timestamp",
            field=models.DateTimeField(
                db_index=True,
                default=django.utils.timezone.now,
                verbose_name="timestamp",
            ),
        ),
    ]
