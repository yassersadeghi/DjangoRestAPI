from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from DevApp.filters import DeveloperFilterset
from DevApp.models import Developer
from DevApp.serializers import DeveloperSerializer

class DeveloperView(ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = DeveloperFilterset
    search_fields = ['FirstName', 'LastName']
    ordering_fields = ['FirstName', 'LastName']