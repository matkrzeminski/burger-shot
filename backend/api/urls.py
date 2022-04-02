from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from ..locations.views import (
    CountryViewSet,
    StateViewSet,
    CityViewSet, LocationListRetrieveAPIView,
)
from ..users.views import UserAPIView, UserAddressViewSet

schema_view = get_schema_view(
    openapi.Info(
        title="Burger shot API",
        default_version="v1",
        description="Burger shot API",
        contact=openapi.Contact(email="admin@burger-shot.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router = DefaultRouter()
router.register("countries", CountryViewSet)
router.register("states", StateViewSet)
router.register("cities", CityViewSet)
# router.register("users/me/addresses", UserAddressViewSet)

urlpatterns = [
    path("users/me/", UserAPIView.as_view(), name="me"),
    path("locations/", LocationListRetrieveAPIView.as_view(), name="locations"),
    path("locations/<uuid:uuid>/", LocationListRetrieveAPIView.as_view(), name="location"),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]

urlpatterns += router.urls
