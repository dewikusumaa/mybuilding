# Generated by Django 3.2.2 on 2021-07-21 07:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210719_0129'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='address',
            field=models.CharField(default=django.utils.timezone.now, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='no_hape',
            field=models.CharField(default=django.utils.timezone.now, max_length=13),
            preserve_default=False,
        ),
    ]
