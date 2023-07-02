from rest_framework import serializers
from .models import About,Goal,CoreBgImage, Capacity,CapacityList, GrassRoot,Academics, VisionMissionValue,InternalSystemList, PartenerLogo, WhereWeWork, PartenerNetwork, InternalSystem, GoalList, Core, History


class AboutSerializer(serializers.ModelSerializer):

    class Meta:
        model = About
        fields = '__all__'
class CoreBgImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = CoreBgImage
        fields = '__all__'
class CapacityListSerializer(serializers.ModelSerializer):

    class Meta:
        model = CapacityList
        fields = '__all__'
class CapacitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Capacity
        fields = '__all__'


class WhereWeWorkSerializer(serializers.ModelSerializer):

    class Meta:
        model = WhereWeWork
        fields = '__all__'
class GrassRootSerializer(serializers.ModelSerializer):

    class Meta:
        model = GrassRoot
        fields = '__all__'

class AcademicsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Academics
        fields = '__all__'


class PartenerLogoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartenerLogo
        fields = '__all__'

class VisionMissionValueSerializer(serializers.ModelSerializer):

    class Meta:
        model = VisionMissionValue
        fields = '__all__'


class PartenerNetworkSerializer(serializers.ModelSerializer):

    class Meta:
        model = PartenerNetwork
        fields = '__all__'
class InternalSystemSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternalSystem
        fields = '__all__'
class InternalSystemListSerializer(serializers.ModelSerializer):

    class Meta:
        model = InternalSystemList
        fields = '__all__'

class GoalListSerializer(serializers.ModelSerializer):

    class Meta:
        model = GoalList
        fields = '__all__'
class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = '__all__'

class CoreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Core
        fields = '__all__'
class HistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = History
        fields = '__all__'