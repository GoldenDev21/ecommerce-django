from rest_framework import serializers
from .models import Address, User


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'primary', 'type', 'line_1', 'line_2', 'city', 'state', 'zip']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'addresses', 'is_on_mailing_list']
