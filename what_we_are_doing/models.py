from django.db import models
from .validators import validate_file_extension, validate_image_extension

# Create your models here.
class WhatWeAreDoing(models.Model):
    image_bg_whatWeAreDoing = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhatWeAreDoing/', blank=True, )

    text_WhatWeAreDoing = models.TextField(
        max_length=1000, default='', blank=True, )
    text_WhatWeAreDoing_ar = models.TextField(
        max_length=1000, default='', blank=True, )

    text_project = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_project_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    image_bg_whatWeAreDoing_project = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', blank=True, )
    text_themes = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_themes_ar = models.TextField(
        max_length=1000, default='',  blank=True,)


class Themes(models.Model):
    image_bg_themes = models.FileField(
        validators=[validate_image_extension], upload_to='background/themes/', blank=True, )
    themes_icons = models.FileField(
        validators=[validate_image_extension], upload_to='background/themes/', blank=True, )
    themes_details_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/themes/', blank=True, ) 
    themes_title = models.CharField(
        max_length=1000, default='', blank=True, )
    themes_title_ar = models.CharField(
        max_length=1000, default='', blank=True, )

    themes_dsc1 = models.TextField(
        max_length=1000, default='', blank=True, )
    themes_dsc1_ar = models.TextField(
        max_length=1000, default='', blank=True, )

    themes_dsc2 = models.TextField(
        max_length=1000, default='', blank=True, )
    themes_dsc2_ar = models.TextField(
        max_length=1000, default='', blank=True, )


