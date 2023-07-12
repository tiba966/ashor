from django.urls import path
from . import views

app_name = 'media'

urlpatterns = [
    path('', views.media_list, name='media'),
  path("media_filter/", views.media_filter, name="media_filter"),

    path("media/<int:id>/", views.media_detail, name="media_detail"),

]
