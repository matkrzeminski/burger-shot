import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

pytestmark = pytest.mark.django_db


def test_user_serializer_get_first_name(user, user_token):
    """
    Test that the first_name is returned in the serializer
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("me")
    response = client.get(url)
    assert response.data["first_name"] == user.first_name


def test_user_serializer_get_last_name(user, user_token):
    """
    Test that the last_name is returned in the serializer
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("me")
    response = client.get(url)
    assert response.data["last_name"] == user.last_name


def test_user_serializer_get_full_name(user, user_token):
    """
    Test that the full_name is returned in the serializer
    """
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("me")
    response = client.get(url)
    assert response.data["full_name"] == user.get_full_name
