# Generated by Django 3.2.2 on 2021-07-31 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_masuk', '0005_rename_adrress_productmasuk_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmasuk',
            name='address',
            field=models.TextField(blank=True),
        ),
    ]
