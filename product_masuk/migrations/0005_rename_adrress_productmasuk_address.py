# Generated by Django 3.2.2 on 2021-07-31 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product_masuk', '0004_rename_name_productmasuk_name_bahan'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmasuk',
            old_name='adrress',
            new_name='address',
        ),
    ]