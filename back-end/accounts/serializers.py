from rest_framework import serializers
from .models import Address, User
from django.contrib.auth.hashers import make_password


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "user",
            "primary",
            "line_1",
            "line_2",
            "city",
            "state",
            "zip",
            "phone",
        ]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        """
        Will return a list of all addresses for the currently authenticated
        user. Otherwise, if the user is an admin, will return all.
        """
        user = self.request.user
        if user.is_staff:
            return Address.objects.all()
        return Address.objects.filter(user=user)


class UserSerializer(serializers.ModelSerializer):
    addresses = AddressSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "addresses",
            "is_on_mailing_list",
            "given_name",
            "family_name",
            'is_staff'
        ]

    def create(self, validated_data):
        validated_data["password"] = make_password(validated_data.get("password"))
        return super(UserSerializer, self).create(validated_data)

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        if "password" in validated_data:
            user.set_password(validated_data["password"])
        user.save()
        return user


class CurrentUserSerializer(UserSerializer):

    class Meta:
        model = User
        exclude = ['password']
