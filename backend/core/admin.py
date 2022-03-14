from django.contrib import admin

from .models import Country, City
from backend.users.models import UserAddress


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country
    list_display = ('name', 'number_of_customers')

    @admin.display(empty_value='0')
    def number_of_customers(self, obj):
        return UserAddress.objects.exclude(user__is_staff=True).filter(country__name=obj.name).select_related().count()


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    list_display = ('name', 'number_of_customers')

    @admin.display(empty_value='0')
    def number_of_customers(self, obj):
        return UserAddress.objects.exclude(user__is_staff=True).filter(city__name=obj.name).select_related().count()
