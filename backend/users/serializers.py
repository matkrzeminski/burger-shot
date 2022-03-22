from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer
from rest_framework import serializers

from backend.users.models import Address

User = get_user_model()


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # addresses = serializers.HyperlinkedRelatedField(
    #     many=True, read_only=True, view_name="user-addresses"
    # )
    first_name = serializers.SerializerMethodField()
    last_name = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "first_name",
            "last_name",
            "full_name",
            "phone_number",
            "is_active",
            # "addresses",
        ]

    def get_first_name(self, obj):
        return obj.first_name.title()

    def get_last_name(self, obj):
        return obj.last_name.title()

    def get_full_name(self, obj):
        return f"{self.get_first_name(obj)} {self.get_last_name(obj)}"


class UserAddressesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"


class CreateUserSerializer(UserCreateSerializer):
    class Meta:
        model = User
        fields = ["email", "password"]
