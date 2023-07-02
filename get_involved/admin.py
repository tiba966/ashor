from django.contrib import admin
from .models import GetInvolved,Volunteer, Donate, CareerDetail, CareerList


class GetInvolvedAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_get_involved',
                    'career_text',
                    'career_text_ar',
                    'Volunteers_text',
                    'Volunteers_text_ar',
                    'Donate_text',
                    'Donate_text_ar',
                    ]
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_volunteer',
'volunteer_text',
'volunteer_text_ar',
                    ]
class DonateAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_donate',
                    'donate_text_support',
                    'donate_text_support_ar',
                    'donate_title',
                    'donate_title_ar',
                    'donate_benefi_1',
                    'donate_benefi_1_ar',
                        'donate_benefi_2',
                    'donate_benefi_2_ar',
                    'donate_benefi_3',
                    'donate_benefi_3_ar',
                    'donate_benefi_4',
                    'donate_benefi_4_ar',
                    ]
class CareerListAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_career_list',
                    ]


class CareerDetatilAdmin(admin.ModelAdmin):
    list_display = ['id',
  
                    'career_name',
                    'career_name_ar',   
                    'career_name',
                    'career_name_ar', 
                    'career_desc',
                    'career_desc_ar', 
                    'career_employee_type',
                    'career_employee_type_ar',   
                    'career_summary_text',
                    'career_summary_text_ar',   
                    'career_duties_text',
                    'career_duties_text_ar',   
                    'job_type',
                    'job_type_ar', 
                    'location',
                    'location_ar',   
                    'duties_1',
                    'duties_1_ar',   
                    'duties_2',
                    'duties_2_ar',   
                    'duties_3',
                    'duties_3_ar',   
                    'duties_4',
                    'duties_4_ar',       
                      'duties_5',
                    'duties_5_ar',  
                      'skill_1',
                    'skill_1_ar',  
                      'skill_2',
                    'skill_2_ar',  
                      'skill_3',
                    'skill_3_ar',  
                      'skill_4',
                    'skill_4_ar',  
                      'skill_5',
                    'skill_5_ar',                ]
                    
                    
                    

admin.site.register(GetInvolved, GetInvolvedAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
admin.site.register(Donate, DonateAdmin)

admin.site.register(CareerList, CareerListAdmin)
admin.site.register(CareerDetail, CareerDetatilAdmin)
