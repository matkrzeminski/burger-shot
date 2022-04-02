from rest_framework import permissions, viewsets, generics, mixins

from .models import Country, State, City
from .serializers import (
    CountrySerializer,
    StateSerializer,
    CitySerializer,
    LocationSerializer,
)


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "uuid"


class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "uuid"


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "uuid"


class LocationListRetrieveAPIView(mixins.RetrieveModelMixin, generics.ListAPIView):
    serializer_class = LocationSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"

    def get_queryset(self):
        uuid = self.kwargs.get("uuid")
        if uuid:
            return Country.objects.filter(uuid=uuid)
        return Country.objects.all()
