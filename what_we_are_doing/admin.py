from django.contrib import admin
from .models import WhatWeAreDoing, Themes



class WhatWeAreDoingeAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_whatWeAreDoing',
                    'text_WhatWeAreDoing',
                    'text_WhatWeAreDoing_ar',
                    'text_project',
                    'text_project_ar',
                     'image_bg_whatWeAreDoing_project',
                    'text_themes',
                    'text_themes_ar',
                    ]

class ThemesAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_themes',
                    'themes_icons',
                    'themes_details_image',
                    'themes_title',
                    'themes_title_ar',
                    'themes_dsc1',
                     'themes_dsc1_ar',
                    'themes_dsc2',
                    'themes_dsc2_ar',
                    ]
admin.site.register(WhatWeAreDoing, WhatWeAreDoingeAdmin)
admin.site.register(Themes, ThemesAdmin)