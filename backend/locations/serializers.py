from rest_framework import serializers

from .models import Country, City, State


class CitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid")

    class Meta:
        model = City
        fields = ["id", "name"]


class StateSerializer(serializers.ModelSerializer):
    cities = CitySerializer(many=True, read_only=True)
    id = serializers.UUIDField(source="uuid")

    class Meta:
        model = State
        fields = ["id", "name", "cities"]


class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)
    id = serializers.UUIDField(source="uuid")

    class Meta:
        model = Country
        fields = ["id", "name", "states"]
