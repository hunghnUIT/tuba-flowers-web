# Generated by Django 2.2.13 on 2020-06-25 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='descrition',
            field=models.TextField(default='', null=True),
        ),
    ]
