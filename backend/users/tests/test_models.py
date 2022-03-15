import pytest

from .factories import UserFactory

pytestmark = pytest.mark.django_db


def test__str__(user, superuser):
    assert user.__str__() == user.email
    assert str(user) == user.email
    assert superuser.__str__() == superuser.email
    assert str(superuser) == superuser.email


def test_get_full_name(user, superuser):
    assert user.get_full_name == f"{user.first_name} {user.last_name}"
    assert superuser.get_full_name == f"{superuser.first_name} {superuser.last_name}"


def test_normalized_email(user, superuser):
    user_email = user.email
    superuser_email = superuser.email
    assert user.email == user_email.lower()
    assert superuser.email == superuser_email.lower()


def test_user(user):
    assert user.is_staff == False
    assert user.is_superuser == False
    assert user.is_active == True


def test_no_email():
    with pytest.raises(ValueError) as error:
        UserFactory(email=None)
    assert str(error.value) == "Valid email address is required for Customers."


def test_invalid_email():
    with pytest.raises(ValueError) as error:
        UserFactory(email="invalid")
    assert str(error.value) == "You must provide a valid email address."


def test_superuser(superuser):
    assert superuser.is_active == True
    assert superuser.is_staff == True
    assert superuser.is_superuser == True


def test_admin_is_not_staff():
    with pytest.raises(ValueError) as error:
        UserFactory(is_superuser=True, is_staff=False)
    assert str(error.value) == "Admins must have is_staff=True."


def test_admin_is_not_superuser():
    with pytest.raises(ValueError) as error:
        UserFactory(is_superuser=False, is_staff=True)
    assert str(error.value) == "Admins must have is_superuser=True."


def test_admin_no_password():
    with pytest.raises(ValueError) as error:
        UserFactory(is_superuser=True, is_staff=True, password=None)
    assert str(error.value) == "Admins must have a password."


def test_admin_no_email():
    with pytest.raises(ValueError) as error:
        UserFactory(is_superuser=True, is_staff=True, email=None)
    assert str(error.value) == "Valid email address is required for Admins."


def test_user_address__str__(user_address):
    assert user_address.__str__() == f"{user_address.street} {user_address.apartment}"
    assert str(user_address) == f"{user_address.street} {user_address.apartment}"
