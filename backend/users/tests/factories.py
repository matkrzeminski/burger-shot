import factory
from django.contrib.auth import get_user_model
from factory import Faker
from factory.django import DjangoModelFactory

from backend.locations.tests.factories import BaseAddressFactory
from backend.users.models import Address


class UserFactory(DjangoModelFactory):
    email = Faker("email")
    first_name = Faker("first_name")
    last_name = Faker("last_name")
    phone_number = Faker("phone_number")
    password = Faker("password", length=20)
    is_active = True
    is_staff = False

    class Meta:
        model = get_user_model()
        django_get_or_create = ["email"]

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)


class UserAddressFactory(BaseAddressFactory):
    user = factory.SubFactory(UserFactory)

    class Meta:
        model = Address
        django_get_or_create = ["user"]
