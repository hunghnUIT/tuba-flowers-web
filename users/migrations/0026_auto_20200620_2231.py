# Generated by Django 3.0.4 on 2020-06-20 15:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20200620_2222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 20, 15, 31, 29, 50088, tzinfo=utc)),
        ),
    ]
