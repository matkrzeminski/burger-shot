import uuid

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from backend.locations.tests.factories import StateFactory, CityFactory

pytestmark = pytest.mark.django_db

# State tests
###############################################################################


def test_state_view_set_create(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-list")
    data = {"name": "New State", "country": state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["message"] == "State created successfully"


def test_state_view_set_create_no_data(superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-list")
    response = client.post(url, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "No data provided"


def test_state_view_set_create_no_country(superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-list")
    data = {"name": "New State"}
    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "Country not provided"


def test_state_view_set_create_no_name(superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-list")
    data = {"country": "New Country"}
    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "Name not provided"


def test_state_view_set_create_invalid_country(superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-list")
    data = {"name": "New State", "country": "Invalid Country"}
    response = client.post(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "Country not found"


def test_state_view_set_create_state_already_exists(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-list")
    data = {"name": state.name, "country": state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "State already exists"


def test_state_view_set_create_no_permission(state, user, user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("state-list")
    data = {"name": "New State", "country": state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 403
    assert response.data["detail"] == "You do not have permission to perform this action."


def test_state_view_set_update(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-detail", kwargs={"uuid": state.uuid})
    data = {"name": "New State", "country": state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 200
    assert response.data["message"] == "State updated successfully"


def test_state_view_set_update_no_data(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-detail", kwargs={"uuid": state.uuid})
    response = client.put(url, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "No data provided"


def test_state_view_set_update_no_name(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-detail", kwargs={"uuid": state.uuid})
    data = {"country": "New Country"}
    response = client.put(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "Name not provided"


def test_state_view_set_update_invalid_country(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-detail", kwargs={"uuid": state.uuid})
    data = {"name": "New State", "country": "Invalid Country"}
    response = client.put(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "Country not found"


def test_state_view_set_update_state_not_found(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-detail", kwargs={"uuid": uuid.uuid4()})
    data = {"name": "New State", "country": state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "State not found"


def test_state_view_set_update_no_permission(state, user, user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("state-detail", kwargs={"uuid": state.uuid})
    data = {"name": "New State", "country": state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 403
    assert response.data["detail"] == "You do not have permission to perform this action."


def test_state_view_set_delete(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-detail", kwargs={"uuid": state.uuid})
    response = client.delete(url, format="json")
    assert response.status_code == 200
    assert response.data["message"] == "State deleted successfully"


def test_state_view_set_delete_no_state(state, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("state-detail", kwargs={"uuid": uuid.uuid4()})
    response = client.delete(url, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "State not found"


def test_state_view_set_delete_no_permission(state, user, user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("state-detail", kwargs={"uuid": state.uuid})
    response = client.delete(url, format="json")
    assert response.status_code == 403
    assert response.data["detail"] == "You do not have permission to perform this action."


# City tests
###############################################################################


def test_city_view_set_create(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    data = {"name": "New City", "state": city.state.name, "country": city.state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 201
    assert response.data["message"] == "City created successfully"


def test_city_view_set_create_no_data(superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    response = client.post(url, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "No data provided"


def test_city_view_set_create_no_name(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    data = {"state": city.state.name, "country": city.state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "Name not provided"


def test_city_view_set_create_no_state(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    data = {"name": "New City", "country": city.state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "State not provided"


def test_city_view_set_create_no_country(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    data = {"name": "New City", "state": city.state.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "Country not provided"


def test_city_view_set_create_invalid_state(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    data = {"name": "New City", "state": "Invalid State", "country": city.state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "State not found"


def test_city_view_set_create_invalid_country(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    data = {"name": "New City", "state": city.state.name, "country": "Invalid Country"}
    response = client.post(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "Country not found"


def test_city_view_set_create_state_and_country_does_not_match(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    new_city = CityFactory()
    data = {"name": "New City", "state": city.state.name, "country": new_city.state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "Country and State doesn't match"


def test_city_view_set_create_country_and_state_does_not_match(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    new_city = CityFactory()
    data = {"name": "New City", "state": new_city.state.name, "country": city.state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "Country and State doesn't match"


def test_city_view_set_create_city_already_exists(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-list")
    data = {"name": "New City", "state": city.state.name, "country": city.state.country.name}
    client.post(url, data, format="json")
    response = client.post(url, data, format="json")
    assert response.status_code == 400
    assert response.data["message"] == "City already exists"


def test_city_view_set_create_no_permissions(city, user, user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("city-list")
    data = {"name": "New City", "state": city.state.name, "country": city.state.country.name}
    response = client.post(url, data, format="json")
    assert response.status_code == 403
    assert response.data["detail"] == "You do not have permission to perform this action."


def test_cty_view_set_update(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-detail", kwargs={"uuid": city.uuid})
    data = {"name": "New City", "state": city.state.name, "country": city.state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 200
    assert response.data["message"] == "City updated successfully"


def test_cty_view_set_update_city_not_found(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-detail", kwargs={"uuid": uuid.uuid4()})
    data = {"name": "New City", "state": city.state.name, "country": city.state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "City not found"


def test_cty_view_set_update_state_not_found(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-detail", kwargs={"uuid": city.uuid})
    data = {"name": "New City", "state": "Invalid State", "country": city.state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "State not found"


def test_cty_view_set_update_country_not_found(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-detail", kwargs={"uuid": city.uuid})
    data = {"name": "New City", "state": city.state.name, "country": "Invalid Country"}
    response = client.put(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "Country not found"


def test_cty_view_set_update_country_and_state_does_not_match(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-detail", kwargs={"uuid": city.uuid})
    new_city = CityFactory()
    data = {"name": "New City", "state": city.state.name, "country": new_city.state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 404
    assert response.data["message"] == "Country and State doesn't match"


def test_cty_view_set_update_no_permissions(city, user, user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("city-detail", kwargs={"uuid": city.uuid})
    data = {"name": "New City", "state": city.state.name, "country": city.state.country.name}
    response = client.put(url, data, format="json")
    assert response.status_code == 403
    assert response.data["detail"] == "You do not have permission to perform this action."


def test_city_view_set_destroy(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-detail", kwargs={"uuid": city.uuid})
    response = client.delete(url)
    assert response.status_code == 200
    assert response.data["message"] == "City deleted successfully"


def test_city_view_set_destroy_city_not_found(city, superuser, superuser_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + superuser_token)
    url = reverse("city-detail", kwargs={"uuid": uuid.uuid4()})
    response = client.delete(url)
    assert response.status_code == 404
    assert response.data["message"] == "City not found"


def test_city_view_delete_no_permissions(city, user, user_token):
    client = APIClient()
    client.credentials(HTTP_AUTHORIZATION="Bearer " + user_token)
    url = reverse("city-detail", kwargs={"uuid": city.uuid})
    response = client.delete(url)
    assert response.status_code == 403
    assert response.data["detail"] == "You do not have permission to perform this action."
