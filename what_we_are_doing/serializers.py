from rest_framework import serializers
from .models import WhatWeAreDoing, Themes, ThemeBackgroundImage
from django.core.mail import send_mail



class WhatWeAreDoingSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhatWeAreDoing
        fields = '__all__'


class ThemeBackgroundImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ThemeBackgroundImage
        fields = '__all__'


class ThemesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Themes
        fields = '__all__'