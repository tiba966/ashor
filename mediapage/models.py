from django.db import models
from .validators import validate_image_extension
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator

from datetime import date



class MediaBackgroundImage(models.Model):
    bg_image_story = models.FileField(
        validators=[validate_image_extension], upload_to='background/story/',default='', blank=True)



class Category(models.Model):
    ar_name = models.CharField(blank=False, null=False, max_length=100)
    en_name = models.CharField(blank=False, null=False, max_length=100)
    dr_name = models.CharField(blank=False, null=False, max_length=100)

    def __str__(self):
        return self.en_name


class MediaDetail(models.Model):

    media_image = models.FileField(
        validators=[validate_image_extension], default='',upload_to='background/media/', blank=True)
   
    date = models.DateField(default=date.today, blank=True)
    media_location = models.CharField(
        max_length=300, default='', blank=True)
    media_location_ar = models.CharField(
        max_length=300, default='', blank=True)
    media_location_dr = models.CharField(
        max_length=300, default='', blank=True)
    media_name = models.CharField(
        max_length=300, default='', blank=True)
    media_name_ar = models.CharField(
        max_length=300, default='', blank=True)
    media_name_dr = models.CharField(
        max_length=300, default='', blank=True)
    category = models.ForeignKey(
        'Category',
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )
    media_desc1 = models.TextField(
        max_length=1000, default='', blank=True)
    media_desc1_ar = models.TextField(
        max_length=1000, default='', blank=True)
    media_desc1_dr = models.TextField(
        max_length=1000, default='', blank=True)

    media_desc2 = models.TextField(
        max_length=1000, default='', blank=True)
    media_desc2_ar = models.TextField(
        max_length=1000, default='', blank=True)
    media_desc2_dr = models.TextField(
        max_length=1000, default='', blank=True)

    media_desc3 = models.TextField(
        max_length=1000, default='', blank=True)
    media_desc3_ar = models.TextField(
        max_length=1000, default='', blank=True)
    media_desc3_dr = models.TextField(
        max_length=1000, default='', blank=True)
    views = models.PositiveIntegerField(default=0, validators=[
            MinValueValidator(0)
    ])

    class Meta:
        ordering = ['-date']

