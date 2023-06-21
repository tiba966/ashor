from django.contrib import admin
from .models import WhatWeAreDoing, Themes, ThemeBackgroundImage, Project, Category



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
class ThemeBackgroundImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                'image_bg_theme'
                    ]

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id',
                'project_image',
                'project_name',
                'project_name_ar',
                'project_date',
                'category',
                'project_location',
                'project_location_ar',
                'project_parteners',
                'project_parteners_ar',
                'project_dsc1',
                'project_dsc1_ar',

                    ]

class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'ar_name',
                    'en_name'

                    ]
admin.site.register(Project, ProjectAdmin)

admin.site.register(WhatWeAreDoing, WhatWeAreDoingeAdmin)
admin.site.register(ThemeBackgroundImage, ThemeBackgroundImageAdmin)
admin.site.register(Category, ProjectCategoryAdmin)

admin.site.register(Themes, ThemesAdmin)