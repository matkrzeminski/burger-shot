import pytest
from django.urls import reverse
from pytest_django.asserts import assertContains

from backend.users.models import UserAddress
from backend.users.tests.factories import UserAddressFactory

pytestmark = pytest.mark.django_db


def test_country_admin_number_of_customers(country, admin_client):
    url = reverse("admin:core_country_changelist")
    response = admin_client.get(url)

    users_addresses = [UserAddressFactory(country=country) for _ in range(10)]
    number_of_customers = (
        UserAddress.objects.exclude(user__is_staff=True)
        .filter(country__name=country.name)
        .count()
    )

    assertContains(response, country.name)
    assert number_of_customers == len(users_addresses)


def test_city_admin_number_of_customers(city, admin_client):
    url = reverse("admin:core_city_changelist")
    response = admin_client.get(url)

    users_addresses = [UserAddressFactory(city=city) for _ in range(10)]
    number_of_customers = (
        UserAddress.objects.exclude(user__is_staff=True)
        .filter(city__name=city.name)
        .count()
    )

    assertContains(response, city.name)
    assert number_of_customers == len(users_addresses)


def test_state_admin_number_of_customers(city, admin_client):
    url = reverse("admin:core_state_changelist")
    response = admin_client.get(url)

    users_addresses = [UserAddressFactory(city=city) for _ in range(10)]
    number_of_customers = (
        UserAddress.objects.exclude(user__is_staff=True)
        .filter(city__state__name=city.state.name)
        .count()
    )

    assertContains(response, city.state.name)
    assert number_of_customers == len(users_addresses)
