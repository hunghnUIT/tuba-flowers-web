# Generated by Django 3.0.4 on 2020-04-19 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20200417_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemimage',
            name='image',
            field=models.ImageField(default='default_product.png', upload_to='product_pics'),
        ),
        migrations.AlterField(
            model_name='itemimage',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='products.Item'),
        ),
    ]
