from django.urls import path
from . import views

app_name = 'get_involved'

urlpatterns = [
    path('', views.get_involved, name='get_involved'),
    path('volunteer/', views.volunteer, name='volunteer'),

    path('donate/', views.donate, name='donate'),
    path('careerlist/', views.career_list, name='career_list'),
    # path('careerdetail/<int:id>', views.career_detail, name='career_detail'),
    # path('careerdetail/<int:career_id>', views.career_detail, name='career_detail'),
    path('careerdetail/<int:id>/', views.career_detail, name='career_detail'),
    # path('themes/<int:theme_id>/', views.theme_detail, name='themes_details'),

]
