from django.contrib import admin
from .models import  MediaBackgroundImage, MediaDetail, Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'ar_name',
                    'en_name',
'dr_name'
                    ]


class MediaBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'bg_image_story',

                    ]


class MediaDetailAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'media_image',
                    'date',
                    'media_location',
                    'media_location_ar',
                    'media_location_dr',
                    'media_name',
                    'media_name_ar',
                    'media_name_dr',
                    'category',
                 
                    'media_desc1',
                    'media_desc1_ar',
                    'media_desc1_dr',
                    'media_desc2',
                    'media_desc2_ar',
                    'media_desc2_dr',
                    'media_desc3',
                    'media_desc3_ar',
                    'media_desc3_dr',
                    'views'
                   
                  
                    ]


admin.site.register(Category, CategoryAdmin)

admin.site.register(MediaDetail, MediaDetailAdmin)

admin.site.register(MediaBackgroundImage, MediaBackgroundImageAdmin)