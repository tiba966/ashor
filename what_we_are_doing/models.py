from django.db import models
from .validators import validate_file_extension, validate_image_extension
from datetime import date

# Create your models here.
class WhatWeAreDoing(models.Model):
    image_bg_whatWeAreDoing = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoing/', blank=True, )

    text_WhatWeAreDoing = models.TextField(
        max_length=1000, default='', blank=True, )
    text_WhatWeAreDoing_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    text_WhatWeAreDoing_dr = models.TextField(
        max_length=1000, default='', blank=True, )

    text_project = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_project_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_project_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
    image_bg_whatWeAreDoing_project = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', blank=True, )
    text_themes = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_themes_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_themes_dr = models.TextField(
        max_length=1000, default='',  blank=True,)

class ThemeBackgroundImage(models.Model):
    image_bg_theme = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoing/', blank=True, )


class Themes(models.Model):
<<<<<<< HEAD
=======
    id = models.AutoField(primary_key=True)
    image_bg_themes = models.FileField(
        validators=[validate_image_extension], upload_to='background/themes/', blank=True, )
>>>>>>> fix_bugs
    themes_icons = models.FileField(
        validators=[validate_image_extension], upload_to='background/themes/', blank=True, )
    themes_details_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/themes/', blank=True, ) 
    themes_title = models.CharField(
        max_length=1000, default='', blank=True, )
    themes_title_ar = models.CharField(
        max_length=1000, default='', blank=True, )
    themes_title_dr = models.CharField(
        max_length=1000, default='', blank=True, )
    themes_dsc1 = models.TextField(
        max_length=1000, default='', blank=True, )
    themes_dsc1_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    themes_dsc1_dr = models.TextField(
        max_length=1000, default='', blank=True, )

    themes_dsc2 = models.TextField(
        max_length=1000, default='', blank=True, )
    themes_dsc2_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    themes_dsc2_dr = models.TextField(
        max_length=1000, default='', blank=True, )

class Category(models.Model):
    ar_name = models.CharField(blank=False, null=False, max_length=100)
    en_name = models.CharField(blank=False, null=False, max_length=100)
    dr_name = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return self.en_name
YEAR = (
    ('2018', "2018"),
    ('2019', "2019"),
        ('2020', "2020"),
        ('2021', "2021"),
        ('2022', "2022"),
        ('2023', "2023"),

)

class Project(models.Model):
 
    project_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/themes/', blank=True, ) 
    project_name = models.CharField(
        max_length=1000, default='', blank=True, )
    project_name_ar = models.CharField(
        max_length=1000, default='', blank=True, )
    project_name_dr = models.CharField(
        max_length=1000, default='', blank=True, )
    project_date = models.DateField(default=date.today, blank=True)
    year = models.CharField(choices=YEAR, max_length=6)

    category =  models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    project_location = models.CharField(
        max_length=300, default='', blank=True)
    project_location_ar = models.CharField(
        max_length=300, default='', blank=True)
    project_location_dr = models.CharField(
        max_length=300, default='', blank=True)
    project_parteners = models.CharField(
        max_length=1000, default='', blank=True, )
    project_parteners_ar = models.CharField(
        max_length=1000, default='', blank=True, )
    project_parteners_dr = models.CharField(
        max_length=1000, default='', blank=True, )
    project_dsc1 = models.TextField(
        max_length=1000, default='', blank=True, )
    project_dsc1_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    project_dsc1_dr = models.TextField(
        max_length=1000, default='', blank=True, )
