from django.contrib import admin

from django.contrib import admin
from .models import About,WhereWeWork,Goal, PartenerLogo, InternalSystemList, VisionMissionValue, PartenerNetwork, InternalSystem, GoalList, Core, History

class AboutAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_about',
                    'textabout_desc1',
                    'textabout_desc1_ar',
                    'textabout_desc2',
                    'textabout_desc2_ar',
                    ]
class InternalSystemListAdmin(admin.ModelAdmin):
    list_display = ['id',
                   
                    'internal_list',
                    'internal_list_ar',
                    ]

class VisionMissionValueAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_vission_mission',
                   
                    'Vission_desc',
                    'Vission_desc_ar',
                    'mission_desc',
                    'mission_desc_ar',
                    ]

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_history',
                    'text_history',
                    'text_history_ar',
                    'text_history1',
                    'text_history1_ar',
                    'text_history2',
                    'text_history2_ar',
                    ]
class GoalsAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'goal_name',
                    'goal_name_ar',
                    'goal_num',
                    'goal_desc',
                    'goal_desc_ar'
                    ]
class WhereWeWorkAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_where_we_work',
                    
                    ]
class CoreAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'core_name',
                    'core_name_ar',
                    'core_image',
                    'core_position',
                    'core_position_ar',
                    'core_desc',
                    'core_desc_ar'
                    ]

class PartenerNetworkAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_partener_network',
                    'partener_desc',
                    'partener_desc_ar',
                    'network_desc',
                    'network_desc_ar',
                    ]

class PartenerLogoAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_partener',
                    ]


class InternalSystemAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_internal_system',
                    'interanl_system_desc',
                    'interanl_system_desc_ar',
                    ]
class GoalAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_goal',
                    'goal_desc',
                    'goal_desc_ar',
                    ]

admin.site.register(VisionMissionValue, VisionMissionValueAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(GoalList, GoalsAdmin)
admin.site.register(Core, CoreAdmin)
admin.site.register(PartenerNetwork, PartenerNetworkAdmin)
admin.site.register(InternalSystem, InternalSystemAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhereWeWork, WhereWeWorkAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(PartenerLogo, PartenerLogoAdmin)

admin.site.register(InternalSystemList, InternalSystemListAdmin)
