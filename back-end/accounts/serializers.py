from rest_framework import serializers
from .models import Address, User
from django.contrib.auth.hashers import make_password


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'primary', 'type', 'line_1', 'line_2', 'city', 'state', 'zip']


class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'addresses', 'is_on_mailing_list', 'given_name', 'family_name']

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if 'password' in validated_data:
            user.set_password(validated_data['password'])
            user.save()
        return user
