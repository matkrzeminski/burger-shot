from django.urls import path, include

from ..locations.views import CountryListAPIView
from ..users.views import UserAPIView

urlpatterns = [
    path("users/me/", UserAPIView.as_view(), name='me'),
    path("locations/", CountryListAPIView.as_view(), name='locations')
]
