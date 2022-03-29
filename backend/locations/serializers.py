from rest_framework import serializers

from .models import Country, City, State


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)

    class Meta:
        model = Country
        fields = ("id", "name")


class StateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)
    country = serializers.ReadOnlyField(source="country.name")

    class Meta:
        model = State
        fields = ("id", "name", "country")


class CitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)
    country = serializers.ReadOnlyField(source="country.name")
    state = serializers.ReadOnlyField(source="state.name")

    class Meta:
        model = City
        fields = ("id", "name", "state", "country")


class LocationStateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)

    class Meta:
        model = State
        fields = ("id", "name")


class LocationsSerializer(serializers.ModelSerializer):
    states = LocationStateSerializer(many=True, read_only=True)
    id = serializers.UUIDField(source="uuid")

    class Meta:
        model = Country
        fields = ("id", "name", "states")
