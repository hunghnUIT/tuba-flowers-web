# Generated by Django 3.0.8 on 2020-07-11 04:28

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0019_auto_20200707_0914'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0049_auto_20200708_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date_ordered',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 11, 4, 28, 13, 187296, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_status',
            field=models.CharField(choices=[('1', 'Waiting Confirmation'), ('2', 'Processing'), ('3', 'Shipping'), ('4', 'Finished'), ('5', 'Requesting Cancel'), ('6', 'Canceled')], default='1', max_length=2),
        ),
        migrations.CreateModel(
            name='ReviewItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.PositiveSmallIntegerField(default=5, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('comment', models.TextField(default='This one is so beautiful.')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Item')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
