from rest_framework import serializers
from .models import  GetInvolved,Volunteer, Donate,CareerDetail,CareerList

class GetInvolvedSerializer(serializers.ModelSerializer):

    class Meta:
        model = GetInvolved
        fields = '__all__'

class VolunteerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Volunteer
        fields = '__all__'

class DonateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Donate
        fields = '__all__'

class CareerDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerDetail
        fields = '__all__'


class CareerListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CareerList
        fields = '__all__'


# class CareerDetatilImageSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = CareerDetatilImage
#         fields = '__all__'
