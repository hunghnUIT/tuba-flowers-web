# Generated by Django 2.2.13 on 2020-06-25 15:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0030_auto_20200625_1643'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itemselection',
            old_name='client_bought_price',
            new_name='price_client_bought',
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 25, 15, 54, 24, 216849, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('P', 'Processing'), ('S', 'Shipping'), ('C', 'Completed'), ('RC', 'Requesting Cancel'), ('AC', 'Canceled')], default='P', max_length=2),
        ),
    ]
