import django_filters
from .models import MediaDetail

class MediaDetailFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name='category__en_name', lookup_expr='exact')

    class Meta:
        model = MediaDetail
        fields = ["category"]
                   
