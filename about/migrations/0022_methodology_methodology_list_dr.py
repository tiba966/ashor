# Generated by Django 4.0.4 on 2023-07-11 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0021_methodology'),
    ]

    operations = [
        migrations.AddField(
            model_name='methodology',
            name='methodology_list_dr',
            field=models.CharField(blank=True, default='', max_length=1000),
        ),
    ]
