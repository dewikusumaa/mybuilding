# Generated by Django 3.2.2 on 2021-07-26 04:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_order_kode_transaksi'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='kode_transaksi',
        ),
    ]