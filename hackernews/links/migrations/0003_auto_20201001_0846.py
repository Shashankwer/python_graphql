# Generated by Django 3.1.1 on 2020-10-01 00:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('links', '0002_links_update_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='update_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 10, 1, 0, 46, 57, 302580, tzinfo=utc)),
        ),
    ]
