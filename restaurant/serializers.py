from .models import MenuItem, Booking
from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = "__all__"


class MenuItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = MenuItem
        fields = "__all__"


class BookingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Booking
        fields = "__all__"
