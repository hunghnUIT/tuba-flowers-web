# Generated by Django 3.0.4 on 2020-04-22 04:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20200422_1119'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemselection',
            old_name='amount',
            new_name='quantity',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 22, 4, 29, 51, 913840, tzinfo=utc)),
        ),
    ]
