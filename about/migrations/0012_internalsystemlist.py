# Generated by Django 4.0.4 on 2023-06-28 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0011_partenerlogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='InternalSystemList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_list', models.TextField(blank=True, default='', max_length=1000)),
                ('internal_list_ar', models.TextField(blank=True, default='', max_length=1000)),
            ],
        ),
    ]
