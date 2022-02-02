from rest_framework import serializers
from .models import CustomUser, Profile, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'primary', 'type', 'line_1', 'line_2', 'city', 'state', 'zip']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    addresses = AddressSerializer(many=True, required=False)

    class Meta:
        model = Profile
        fields = ['user', 'mailing_list', 'addresses']
