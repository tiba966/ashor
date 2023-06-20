from django.contrib import admin
from .models import  Slider, Index, Contact, Slider



class SliderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'slide_image_index',
                    'slide_title_index',
                    'slide_title_index_ar',
                    'slide_subtitle_index',
                    'slide_subtitle_index_ar',
                    'slide_dsc_index',
                    'slide_dsc_index_ar',
                    'slide_num_index',

                    ]



class ContactAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'contact_bg_image',
               

                    ]
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'slide_image_index',
                    'slide_title_index',
                    'slide_subtitle_index',
                     'slide_title_index_ar',
                    'slide_subtitle_index_ar',
'slide_num_index',
                    ]

class IndexAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about_index',
                     'text_about_index_ar',
                     'num_employee_index',
                     'num_project_index',
                     'num_benefi_index',
                     'num_volunteer_index',
                  



                    ]



admin.site.register(Index, IndexAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Slider, SliderAdmin)

