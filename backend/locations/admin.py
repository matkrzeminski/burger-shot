from django.contrib import admin

from .models import Country, City, State
from backend.users.models import Address


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ("uuid", "name", "number_of_customers")

    @admin.display(empty_value="0")
    def number_of_customers(self, obj):
        return (
            Address.objects.exclude(user__is_staff=True)
            .filter(country__name=obj.name)
            .count()
        )


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ("uuid", "name", "country", "state", "number_of_customers")

    @admin.display(empty_value="0")
    def number_of_customers(self, obj):
        return (
            Address.objects.exclude(user__is_staff=True)
            .filter(city__name=obj.name)
            .count()
        )


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    model = City
    list_display = ("uuid", "name", "country", "number_of_customers")

    @admin.display(empty_value="0")
    def number_of_customers(self, obj):
        return (
            Address.objects.exclude(user__is_staff=True)
            .filter(city__state__name=obj.name)
            .count()
        )
