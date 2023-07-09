from django.contrib import admin
from .models import  Slider, Index, Contact, Slider







class ContactAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'contact_bg_image',
               

                    ]
class SliderAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'slide_image_index',
                    'slide_title_index',
       'slide_title_index_ar',
                    'slide_title_index_dr',
                    'slide_subtitle_index',
                    'slide_subtitle_index_ar',
                    'slide_subtitle_index_dr',
'slide_num_index',
                    ]

class IndexAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'text_about_index',
                     'text_about_index_ar',
                     'text_about_index_dr',
                     'num_employee_index',
                     'num_project_index',
                     'num_benefi_index',
                     'num_volunteer_index',
               'text_themes_index',
                     'text_themes_index_ar',
                     'text_themes_index_dr',

                    'text_media_index',
                     'text_media_index_ar',
'text_media_index_dr'
                    ]



admin.site.register(Index, IndexAdmin)
admin.site.register(Contact, ContactAdmin)
admin.site.register(Slider, SliderAdmin)

