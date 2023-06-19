import django_filters
from .models import Core


class CoreDetailFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains')
    description = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Core
        fields = '__all__'
        exclude = ['id', 
                    'core_image',
                   ]
