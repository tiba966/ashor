from django.urls import include, path

from . import views
from . import api


app_name = 'home'

urlpatterns = [
    path('', views.index, name='index'),
 
    path('contact', views.contact, name='contact'),

]
