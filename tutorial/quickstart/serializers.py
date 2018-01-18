from django.contrib.auth.models import User, Group
from models import Car, Living
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('make', 'model', 'year', 'plate', 'color')

class LivingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Living
        fields = ('city', 'district', 'house', 'heating', 'cost')
