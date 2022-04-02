

import pytest
from rest_framework.reverse import reverse
from rest_framework.test import APIClient

from backend.locations.tests.factories import StateFactory, CityFactory

pytestmark = pytest.mark.django_db


# TODO: test get_query_set()
