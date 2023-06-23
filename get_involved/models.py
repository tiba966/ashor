from django.db import models
from .validators import validate_image_extension
from datetime import date
from django.utils.translation import gettext_lazy as _


class GetInvolved(models.Model):
    image_bg_get_involved = models.FileField(
        validators=[validate_image_extension], upload_to='background/GetInvolved/', null=True, blank=True)

    career_text = models.TextField(max_length=1000, default='', null=True, blank=True)
    career_text_ar = models.TextField(max_length=1000, default='', null=True, blank=True)
    Volunteers_text = models.TextField(null=True, blank=True)
    Volunteers_text_ar = models.TextField(null=True, blank=True)

    Donate_text = models.TextField(null=True, blank=True)
    Donate_text_ar = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.career_text

class Volunteer(models.Model):
    image_bg_volunteer = models.FileField(
        validators=[validate_image_extension], upload_to='background/GetInvolved/', )

    volunteer_text = models.TextField(null=True, blank=True)
    volunteer_text_ar = models.TextField(null=True, blank=True)

class Donate(models.Model):
    image_bg_donate = models.FileField(
        validators=[validate_image_extension], upload_to='background/GetInvolved/', )

    donate_text_support = models.TextField(null=True, blank=True)
    donate_text_support_ar = models.TextField(null=True, blank=True)

    donate_title = models.CharField(max_length=1000,null=True, blank=True)
    donate_title_ar = models.CharField(max_length=1000,null=True, blank=True)

  
    donate_benefi_1 = models.TextField(null=True, blank=True)
    donate_benefi_1_ar = models.TextField(null=True, blank=True)

    donate_benefi_2 = models.TextField(null=True, blank=True)
    donate_benefi_2_ar = models.TextField(null=True, blank=True)
    donate_benefi_3 = models.TextField(null=True, blank=True)
    donate_benefi_3_ar = models.TextField(null=True, blank=True)
    donate_benefi_4 = models.TextField(null=True, blank=True)
    donate_benefi_4_ar = models.TextField(null=True, blank=True)

JOB_TYPE = (
    ('1', "Full time"),
    ('2', "Part time"),
    ('3', "Internship"),
)

JOB_TYPE_AR = (
    ('1', "دوام كامل"),
    ('2', "دوام جزئي"),
    ('3', "تدريب"),
)
class CareerDetail(models.Model):
    id = models.AutoField(primary_key=True)
    career_name = models.CharField(max_length=300, default='', null=True, blank=True)
    career_name_ar = models.CharField(max_length=300, default='', null=True, blank=True)
    career_desc = models.CharField(max_length=300, default='', null=True, blank=True)
    career_desc_ar = models.CharField(max_length=300, default='', null=True, blank=True)

    career_employee_type = models.CharField(max_length=300, default='', null=True, blank=True)
    career_employee_type_ar = models.CharField(max_length=300, default='', null=True, blank=True)
    
    career_summary_text = models.TextField(null=True, blank=True)
    career_summary_text_ar = models.TextField(null=True, blank=True)
    career_duties_text = models.TextField(null=True, blank=True)
    career_duties_text_ar = models.TextField(null=True, blank=True)

 

    job_type = models.CharField(
        choices=JOB_TYPE, max_length=1, null=True, blank=True)
    job_type_ar = models.CharField(
        choices=JOB_TYPE_AR, max_length=1, null=True, blank=True)
    
    location = models.CharField(
        max_length=300, default='', null=True, blank=True)
    location_ar = models.CharField(
        max_length=300, default='', null=True, blank=True)
   
    no_of_jobs = models.PositiveIntegerField(default=1, null=True, blank=True)
 
       # Roles and Resposibilities
    duties_1 = models.TextField(null=True, blank=True)
    duties_1_ar = models.TextField(null=True, blank=True)
    duties_2 = models.TextField(null=True, blank=True)
    duties_2_ar = models.TextField(null=True, blank=True)
    duties_3 = models.TextField(null=True, blank=True)
    duties_3_ar = models.TextField(null=True, blank=True)
    duties_4 = models.TextField(null=True, blank=True)
    duties_4_ar = models.TextField(null=True, blank=True)
    duties_5 = models.TextField(null=True, blank=True)
    duties_5_ar = models.TextField(null=True, blank=True)
 

   

    # Qualifications & Preferred Skills
    skill_1 = models.TextField(null=True, blank=True)
    skill_1_ar = models.TextField(null=True, blank=True)
    skill_2 = models.TextField(null=True, blank=True)
    skill_2_ar = models.TextField(null=True, blank=True)
    skill_3 = models.TextField(null=True, blank=True)
    skill_3_ar = models.TextField(null=True, blank=True)
    skill_4 = models.TextField(null=True, blank=True)
    skill_4_ar = models.TextField(null=True, blank=True)
    skill_5 = models.TextField(null=True, blank=True)
    skill_5_ar = models.TextField(null=True, blank=True)


    

    def __str__(self):
        return self.career_name


class CareerList(models.Model):
    image_bg_career_list = models.FileField(
        validators=[validate_image_extension], upload_to='background/career_list/', null=True, blank=True)

