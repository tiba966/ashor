from django.contrib import admin

from django.contrib import admin
from .models import About,Resources, Assesments, Roles, People, Polies, WhereWeWork,WhereWeWorkBackground,MethodologyList,Methodology, CoreBgImage,Capacity,CapacityList, Goal,GrassRoot, Academics, PartenerLogo, InternalSystemList, VisionMissionValue, PartenerNetwork, InternalSystem, GoalList, Core, History

class MethodologyListAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'methodology_list',
                    'methodology_list_ar',
                    'methodology_list_dr',
                  
                    ]

class MethodologyAdmin(admin.ModelAdmin):
    list_display = ['id',
    'image_banner_methodology',
                    'methodology_desc',
                    'methodology_desc_ar',
                    'methodology_desc_dr',
                  
                    ]
class AboutAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_about',
                    'textabout_desc1',
                    'textabout_desc1_ar',
                    'textabout_desc1_dr',
                    'textabout_desc2',
                    'textabout_desc2_ar',
                    'textabout_desc2_dr'
                    ]
class CoreBgImageAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_core',
                    'textcore_desc1',
                    'textcore_desc1_ar',
                    'textcore_desc1_dr'
                    ]
class CapacityListAdmin(admin.ModelAdmin):
    list_display = ['id',
                   
                    'capacity_list',
                    'capacity_list_ar',
                    'capacity_list_dr'
                    ]
class CapacityAdmin(admin.ModelAdmin):
    list_display = ['id',
                   'image_banner_capacity',
                    'capacity_desc',
                    'capacity_desc_ar',
                    'capacity_desc_dr',
                    'capacity_desc1',
                    'capacity_desc1_ar',
                    'capacity_desc1_dr'
                    ]
class InternalSystemListAdmin(admin.ModelAdmin):
    list_display = ['id',
                   
                    'internal_list',
                    'internal_list_ar',
                    'internal_list_dr'
                    ]
                    
class VisionMissionValueAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_bg_vission_mission',
                   
                    'Vission_desc',
                    'Vission_desc_ar',
                    'Vission_desc_dr',
                    'mission_desc',
                    'mission_desc_ar',
                    'mission_desc_dr'
                    ]

class HistoryAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_history',
                    'text_history',
                    'text_history_ar',
                    'text_history_dr',
                    'text_history1',
                    'text_history1_ar',
                    'text_history1_dr',
                    'text_history2',
                    'text_history2_ar',
                    'text_history2_dr'
                    ]
class GoalsAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'goal_name',
                    'goal_name_ar',
                    'goal_name_dr',
                    'goal_num',
                    'goal_desc',
                    'goal_desc_ar',
                    'goal_desc_dr'
                    ]
class WhereWeWorkBackgroundAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_where_we_work',
                    ]
class WhereWeWorkAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'address',
                    'address_ar',
                    'address_dr',
                    'address_num',
                    'governorate',
                    'governorate_ar',
                    'governorate_dr',
                    
                    ]
class CoreAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'core_name',
                    'core_name_ar',
                    'core_name_dr',
                    'core_image',
                    'core_position',
                    'core_position_ar',
                    'core_position_dr',
                    'core_desc',
                    'core_desc_ar',
                    'core_desc_dr'
                    ]

class GrassRootAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_grassRoot',
                    'grassRoot_desc',
                    'grassRoot_desc_ar',
                    'grassRoot_desc_dr'
                                    ]
                    


class AcademicsAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_academics',
              
                    'academics_desc',
                    'academics_desc_ar',
                    'academics_desc_dr'
                
                    ]

class PartenerNetworkAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_partener_network',
                    'partener_desc',
                    'partener_desc_ar',
                    'partener_desc_dr',
                    'network_desc',
                    'network_desc_ar',
                    'network_desc_dr'
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
                    'interanl_system_desc_dr'
                    ]
class GoalAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_goal',
                    'goal_desc',
                    'goal_desc_ar',
      'goal_desc_dr',

                    ]
class RolesAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_roles',
                    'text_roles',
                    'text_roles_ar',
      'text_roles_dr',

                    ]
class ResourcesAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_resourc',
                    'text_resourc',
                    'text_resourc_ar',
      'text_resourc_dr',

                    ]
class PoliesAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_polies',
                    'text_polies',
                    'text_polies_ar',
      'text_polies_dr',

                    ]

class AssesmentsAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_assesments',
                    'text_assesments',
                    'text_assesments_ar',
      'text_assesments_dr',

                    ]
class PeopleAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'image_banner_people',
                    'text_people',
                    'text_people_ar',
      'text_people_dr',

                    ]

admin.site.register(People, PeopleAdmin)

admin.site.register(Polies, PoliesAdmin)
admin.site.register(Assesments, AssesmentsAdmin)
admin.site.register(Roles, RolesAdmin)

admin.site.register(VisionMissionValue, VisionMissionValueAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(GoalList, GoalsAdmin)
admin.site.register(Core, CoreAdmin)
admin.site.register(PartenerNetwork, PartenerNetworkAdmin)
admin.site.register(Resources, ResourcesAdmin)

admin.site.register(InternalSystem, InternalSystemAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(WhereWeWork, WhereWeWorkAdmin)
admin.site.register(Goal, GoalAdmin)
admin.site.register(MethodologyList, MethodologyListAdmin)
admin.site.register(Methodology, MethodologyAdmin)
admin.site.register(WhereWeWorkBackground, WhereWeWorkBackgroundAdmin)

admin.site.register(PartenerLogo, PartenerLogoAdmin)
admin.site.register(Academics, AcademicsAdmin)
admin.site.register(GrassRoot, GrassRootAdmin)
admin.site.register(Capacity, CapacityAdmin)
admin.site.register(CapacityList, CapacityListAdmin)
admin.site.register(CoreBgImage, CoreBgImageAdmin)

admin.site.register(InternalSystemList, InternalSystemListAdmin)
