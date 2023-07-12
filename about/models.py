from django.db import models
from .validators import validate_file_extension, validate_image_extension
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


class About(models.Model):
    image_bg_about = models.FileField(
        validators=[validate_image_extension], upload_to='background/vission_mission/', )
    textabout_desc1 = models.TextField(
        max_length=1000, default='', blank=True, )
    textabout_desc1_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    textabout_desc1_dr = models.TextField(
        max_length=1000, default='', blank=True, )
    textabout_desc2 = models.TextField(
        max_length=1000, default='', blank=True, )
    textabout_desc2_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    textabout_desc2_dr = models.TextField(
        max_length=1000, default='', blank=True, )


class CoreBgImage(models.Model):
    image_bg_core = models.FileField(
        validators=[validate_image_extension], upload_to='background/vission_mission/', )
    textcore_desc1 = models.TextField(
        max_length=1000, default='', blank=True, )
    textcore_desc1_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    textcore_desc1_dr = models.TextField(
        max_length=1000, default='', blank=True, )
class VisionMissionValue(models.Model):
    image_bg_vission_mission = models.FileField(
        validators=[validate_image_extension], upload_to='background/vission_mission/', )

        
    Vission_desc = models.TextField(
        max_length=1000, default='', blank=True, )
    Vission_desc_ar = models.TextField(
        max_length=1000, default='', blank=True, )
    Vission_desc_dr = models.TextField(
        max_length=1000, default='', blank=True, )
    mission_desc = models.TextField(
        max_length=1000, default='', blank=True, )
    mission_desc_ar = models.TextField(
        max_length=1000, default='', blank=True, )  
    mission_desc_dr = models.TextField(
        max_length=1000, default='', blank=True, )  
class History(models.Model):
    image_banner_history = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', )
    text_history = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history1 = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history1_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history1_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history2 = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history2_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    text_history2_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
class Goal(models.Model):
    image_banner_goal = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', )
   
    goal_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    goal_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    goal_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
  
class MethodologyList(models.Model):
    methodology_list = models.CharField(
        max_length=1000, default='',  blank=True,)
    methodology_list_ar = models.CharField(
        max_length=1000, default='',  blank=True,)
    methodology_list_dr = models.CharField(
        max_length=1000, default='',  blank=True,)
   
class Methodology(models.Model):
    image_banner_methodology  = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', )
   
    methodology_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    methodology_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    methodology_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
        

class GoalList(models.Model):
    goal_name = models.CharField(
        max_length=1000, default='',  blank=True,)
    goal_name_ar = models.CharField(
        max_length=1000, default='',  blank=True,)
    goal_name_dr = models.CharField(
        max_length=1000, default='',  blank=True,)
    goal_num = models.CharField(
        max_length=1000, default='',  blank=True,)
    goal_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    goal_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    goal_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)

# class Capacity(models.Model):
    # image_banner_capacity  = models.FileField(
    #     validators=[validate_image_extension], upload_to='background/about/', )
   
    # capacity_desc = models.TextField(
    #     max_length=1000, default='',  blank=True,)
    # capacity_desc_ar = models.TextField(
    #     max_length=1000, default='',  blank=True,)
    # capacity_desc_dr = models.TextField(
    #     max_length=1000, default='',  blank=True,)
        
class Capacity(models.Model):
    image_banner_capacity  = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', )
   
    capacity_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    capacity_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    capacity_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
    capacity_desc1 = models.TextField(
        max_length=1000, default='',  blank=True,)
    capacity_desc1_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    capacity_desc1_dr = models.TextField(
        max_length=1000, default='',  blank=True,)

  
  
class CapacityList(models.Model):
    capacity_list = models.CharField(
        max_length=1000, default='',  blank=True,)
    capacity_list_ar = models.CharField(
        max_length=1000, default='',  blank=True,)
    capacity_list_dr = models.CharField(
        max_length=1000, default='',  blank=True,)
class Core(models.Model):
   
    core_name = models.CharField(
        max_length=1000, default='',  blank=True,)
    core_name_ar = models.CharField(
        max_length=1000, default='',  blank=True,)
    core_name_dr = models.CharField(
        max_length=1000, default='',  blank=True,)
    core_image = models.FileField(
        validators=[validate_image_extension], upload_to='background/about/', )
    core_position = models.CharField(
        max_length=1000, default='',  blank=True,)
    core_position_ar = models.CharField(
        max_length=1000, default='',  blank=True,)
    core_position_dr = models.CharField(
        max_length=1000, default='',  blank=True,)
    core_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    core_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    core_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)


class PartenerLogo(models.Model):
    image_partener = models.FileField(
        validators=[validate_image_extension], upload_to='background/PartenerNetwork/', )


class PartenerNetwork(models.Model):
    image_banner_partener_network = models.FileField(
        validators=[validate_image_extension], upload_to='background/PartenerNetwork/', )
    partener_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    partener_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    partener_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
    network_desc = models.CharField(
        max_length=1000, default='',  blank=True,)
    network_desc_ar = models.CharField(
        max_length=1000, default='',  blank=True,)
    network_desc_dr = models.CharField(
        max_length=1000, default='',  blank=True,)


class WhereWeWork(models.Model):
    image_banner_where_we_work = models.FileField(
        validators=[validate_image_extension], upload_to='background/WhereWeWork/', )

class InternalSystemList(models.Model):
    internal_list = models.TextField(
        max_length=1000, default='',  blank=True,)
    internal_list_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    internal_list_dr = models.TextField(
        max_length=1000, default='',  blank=True,)

class GrassRoot(models.Model):
    image_banner_grassRoot = models.FileField(
        validators=[validate_image_extension], upload_to='background/InternalSystem/', )
    grassRoot_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    grassRoot_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    grassRoot_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
class Academics (models.Model):
    image_banner_academics  = models.FileField(
        validators=[validate_image_extension], upload_to='background/InternalSystem/', )
    academics_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    academics_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)
    academics_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)

   

class InternalSystem(models.Model):
    image_banner_internal_system = models.FileField(
        validators=[validate_image_extension], upload_to='background/InternalSystem/', )
    interanl_system_desc = models.TextField(
        max_length=1000, default='',  blank=True,)
    interanl_system_desc_ar = models.TextField(
        max_length=1000, default='',  blank=True,)

    interanl_system_desc_dr = models.TextField(
        max_length=1000, default='',  blank=True,)
