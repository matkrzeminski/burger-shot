from rest_framework import serializers

from .models import Country, City, State


class CountrySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)

    class Meta:
        model = Country
        fields = ("id", "name")


class StateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)
    country = CountrySerializer()

    class Meta:
        model = State
        fields = ("id", "name", "country")

    def create(self, validated_data):
        country_data = validated_data.pop("country")
        country = Country.objects.get_or_create(**country_data)[0]
        state = State.objects.create(country=country, **validated_data)
        return state


class CitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)
    state = StateSerializer()

    class Meta:
        model = City
        fields = ("id", "name", "state")

    def create(self, validated_data):
        state_data = validated_data.pop("state")
        state = State.objects.get_or_create(**state_data)[0]
        city = City.objects.create(state=state, **validated_data)
        return city


class LocationCitySerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)

    class Meta:
        model = City
        fields = ("id", "name")


class LocationStateSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)
    cities = LocationCitySerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ("id", "name", "cities")


class LocationSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(source="uuid", read_only=True)
    states = LocationStateSerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ("id", "name", "states")
