from rest_framework import serializers

from DevApp.models import Developer


class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'