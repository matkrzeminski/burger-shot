import pytest

pytestmark = pytest.mark.django_db


def test_country__str__(country):
    assert country.__str__() == country.name
    assert str(country) == country.name


def test_city__str__(city):
    assert city.__str__() == city.name
    assert str(city) == city.name


def test_state__str__(state):
    assert state.__str__() == state.name
    assert str(state) == state.name
