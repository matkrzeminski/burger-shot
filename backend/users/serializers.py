from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers
from rest_framework.response import Response

from backend.locations.models import Country, City
from backend.users.models import Address

User = get_user_model()


class UserAddressSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source="city.name")
    country = serializers.CharField(source="country.name")
    state = serializers.CharField(source="city.state.name", read_only=True)
    id = serializers.UUIDField(source="uuid", read_only=True)

    class Meta:
        model = Address
        fields = [
            "id",
            "name",
            "postcode",
            "city",
            "state",
            "street",
            "apartment",
            "country",
            "created",
            "modified",
        ]


class UserSerializer(serializers.ModelSerializer):
    addresses = UserAddressSerializer(many=True, read_only=True)
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()
    id = serializers.UUIDField(source="uuid")

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "phone_number",
            "is_active",
            "addresses",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def get_full_name(self, obj):
        return f"{self.get_first_name(obj)} {self.get_last_name(obj)}"


class CreateUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
