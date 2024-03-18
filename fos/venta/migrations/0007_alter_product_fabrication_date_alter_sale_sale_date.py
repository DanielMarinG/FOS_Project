# Generated by Django 4.2.7 on 2024-03-18 20:13

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('venta', '0006_alter_product_fabrication_date_alter_sale_sale_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='fabrication_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2024, 3, 18))], verbose_name='Fecha Fabricación'),
        ),
        migrations.AlterField(
            model_name='sale',
            name='sale_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2024, 3, 18))], verbose_name='Fecha Venta'),
        ),
    ]