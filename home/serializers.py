from rest_framework import serializers
from .models import Slider, Index, Contact, Slider
from django.core.mail import send_mail



class IndexSerializer(serializers.ModelSerializer):

    class Meta:
        model = Index
        fields = '__all__'
class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contact
        fields = '__all__'

class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'


class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Slider
        fields = '__all__'