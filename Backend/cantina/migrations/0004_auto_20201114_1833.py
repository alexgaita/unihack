# Generated by Django 3.1.3 on 2020-11-14 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantina', '0003_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
