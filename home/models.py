from django.db import models
from .validators import validate_file_extension, validate_image_extension
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _

   

class Contact(models.Model):
    contact_bg_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
class Index(models.Model):
    
    text_about_index = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about_index_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_about_index_dr = models.TextField(
        max_length=1000, default='',  blank=True,)

    num_employee_index = models.CharField(
        max_length=1000, default='',  blank=True,) 
    num_project_index = models.CharField(
        max_length=1000, default='',  blank=True,) 
    num_benefi_index = models.CharField(
        max_length=1000, default='',  blank=True,) 
    num_volunteer_index = models.CharField(
        max_length=1000, default='',  blank=True,) 
    text_themes_index = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_themes_index_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_themes_index_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_media_index = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_media_index_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_media_index_dr = models.TextField(
        max_length=1000, default='',  blank=True,)

class Slider(models.Model):
    slide_image_index = models.FileField(
        validators=[validate_image_extension], upload_to='background/index/', blank=True, )
    slide_title_index = models.CharField(
        max_length=300, default='', blank=True, )
    slide_title_index_ar = models.CharField(
        max_length=300, default='', blank=True, )
    slide_title_index_dr = models.CharField(
        max_length=300, default='', blank=True, )
    slide_subtitle_index = models.CharField(
        max_length=300, default='', blank=True, )
    slide_subtitle_index_ar = models.CharField(
        max_length=300, default='', blank=True, )
    slide_subtitle_index_dr = models.CharField(
        max_length=300, default='', blank=True, )
    slide_num_index = models.CharField(
        max_length=300, default='', blank=True, )

