# Generated by Django 4.0.4 on 2023-06-17 20:32

from django.db import migrations, models
import get_involved.validators


class Migration(migrations.Migration):

    dependencies = [
        ('get_involved', '0003_volunteer_volunteer_text_volunteer_volunteer_text_ar'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_bg_donate', models.FileField(upload_to='background/volunteer/', validators=[get_involved.validators.validate_image_extension])),
                ('donate_text_support', models.TextField(blank=True, null=True)),
                ('donate_text_support_ar', models.TextField(blank=True, null=True)),
                ('donate_title', models.CharField(blank=True, max_length=1000, null=True)),
                ('donate_title_ar', models.CharField(blank=True, max_length=1000, null=True)),
                ('donate_benefi_1', models.TextField(blank=True, null=True)),
                ('donate_benefi_1_ar', models.TextField(blank=True, null=True)),
                ('donate_benefi_2', models.TextField(blank=True, null=True)),
                ('donate_benefi_2_ar', models.TextField(blank=True, null=True)),
                ('donate_benefi_3', models.TextField(blank=True, null=True)),
                ('donate_benefi_3_ar', models.TextField(blank=True, null=True)),
                ('donate_benefi_4', models.TextField(blank=True, null=True)),
                ('donate_benefi_4_ar', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
