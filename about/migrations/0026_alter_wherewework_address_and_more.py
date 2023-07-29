# Generated by Django 4.0.4 on 2023-07-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0025_wherewework_governorate_wherewework_governorate_ar_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wherewework',
            name='address',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='wherewework',
            name='address_ar',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='wherewework',
            name='address_dr',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='wherewework',
            name='address_num',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='wherewework',
            name='governorate',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='wherewework',
            name='governorate_ar',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='wherewework',
            name='governorate_dr',
            field=models.CharField(blank=True, default='', max_length=500),
        ),
    ]