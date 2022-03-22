import pytest

from .locations.tests.factories import CountryFactory, CityFactory, StateFactory
from .users.tests.factories import UserFactory, UserAddressFactory


@pytest.fixture()
def user():
    return UserFactory()


@pytest.fixture()
def superuser():
    return UserFactory(is_superuser=True, is_staff=True)


@pytest.fixture()
def country():
    return CountryFactory()


@pytest.fixture()
def state():
    return StateFactory()


@pytest.fixture()
def city():
    return CityFactory()


@pytest.fixture()
def user_address():
    return UserAddressFactory()
