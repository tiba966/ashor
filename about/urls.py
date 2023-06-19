from django.urls import path
from . import views
from django.contrib import admin
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
        path('goals/', views.goals, name='goals'),
        path('history/', views.history, name='history'),
        path('vission_mission/', views.vission_mission, name='vission_mission'),
        path('partener_network/', views.partener_network, name='partener_network'),
        path('internal_system/', views.internal_system, name='internal_system'),
        path('where_we_work/', views.where_we_work, name='where_we_work'),
        path('core_list/', views.core_list, name='core_list'),
        path('core_detail/<int:id>', views.core_detail, name='core_detail'),

   
]
