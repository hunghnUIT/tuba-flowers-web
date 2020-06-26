# Generated by Django 2.2.13 on 2020-06-25 09:43

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0029_merge_20200625_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='itemselection',
            name='client_bought_price',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 25, 9, 43, 12, 744260, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('P', 'Processing'), ('S', 'Shipping'), ('C', 'Completed'), ('RC', 'Requesting Cancel'), ('AC', 'Accepted Cancellation Request')], default='P', max_length=2),
        ),
    ]