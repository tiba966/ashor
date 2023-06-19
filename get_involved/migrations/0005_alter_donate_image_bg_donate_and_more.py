# Generated by Django 4.0.4 on 2023-06-17 20:35

from django.db import migrations, models
import get_involved.validators


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0004_donate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donate',
            name='image_bg_donate',
            field=models.FileField(upload_to='background/GetInvolved/', validators=[get_involved.validators.validate_image_extension]),
        ),
        migrations.AlterField(
            model_name='volunteer',
            name='image_bg_volunteer',
            field=models.FileField(upload_to='background/GetInvolved/', validators=[get_involved.validators.validate_image_extension]),
        ),
    ]
