from django.urls import path
from . import views

app_name = 'what_we_are_doing'

urlpatterns = [
    path('', views.what_we_are_doing, name='what_we_are_doing'),
   
    path('themes/', views.themes, name='themes'),
    # path('themes_details/<int:id>', views.themes_details, name='themes_details'),
    # path('themes/<int:id>/', views.theme_detail, name='themes_details'),
    path('themes/<int:theme_id>/', views.theme_detail, name='themes_details'),
    path('project/', views.project, name='project'),
]
