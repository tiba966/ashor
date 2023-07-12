import django_filters
from .models import Themes, Project


class ThemesDetailFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Themes
        fields = '__all__'
        exclude = [
            'id',
            'image_bg_themes',
            'themes_icons',
            'themes_details_image',

        ]


class ProjectDetailFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__en_name', lookup_expr='exact')

    class Meta:
        model = Project
        fields = ["category"]
                   

