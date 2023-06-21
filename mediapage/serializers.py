from rest_framework import serializers
from .models import  MediaBackgroundImage, MediaDetail





class MediaBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaBackgroundImage
        fields = '__all__'


class MediaDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = MediaDetail
        fields = '__all__'
        ordering = ['-date']
