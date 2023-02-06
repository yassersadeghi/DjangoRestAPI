from django_filters.rest_framework import FilterSet

from DevApp.models import Developer


class DeveloperFilterset(FilterSet):
    class Meta:
        model = Developer
        fields = {
            'FirstName': ['exact'],
            'LastName': ['exact'],
            'Years': ['gt','lt'],
        }