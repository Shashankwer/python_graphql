# Generated by Django 3.1.1 on 2020-10-01 03:32

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0003_auto_20201001_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 1, 3, 32, 20, 533891, tzinfo=utc)),
        ),
    ]
