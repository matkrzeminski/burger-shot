import factory
from factory import Faker
from factory.django import DjangoModelFactory

from ..models import Country, City, Address, State


class CountryFactory(DjangoModelFactory):
    name = Faker("country")

    class Meta:
        model = Country
        django_get_or_create = ["name"]


class StateFactory(DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    name = Faker("state")

    class Meta:
        model = State
        django_get_or_create = ["name"]


class CityFactory(DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    state = factory.SubFactory(StateFactory)
    name = Faker("city")

    class Meta:
        model = City
        django_get_or_create = ["name"]


class AddressFactory(DjangoModelFactory):
    country = factory.SubFactory(CountryFactory)
    city = factory.SubFactory(CityFactory)
    postcode = Faker("postcode")
    street = Faker("street_name")
    apartment = factory.Iterator([123, "12a", "32", "", 9, "2213", 2213])

    class Meta:
        model = Address
        django_get_or_create = ["country", "city"]
