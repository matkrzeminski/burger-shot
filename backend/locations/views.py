from rest_framework import permissions, status, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.response import Response


from .models import Country, State, City
from .serializers import (
    LocationsSerializer,
    CountrySerializer,
    StateSerializer,
    CitySerializer,
)


class LocationsListAPIView(ListAPIView):
    """
    Lists all available locations.
    """

    queryset = Country.objects.all()
    serializer_class = LocationsSerializer
    permission_classes = [permissions.IsAuthenticated]


class CountryViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing countries.

    create:
    Create a new country.

    retrieve:
    Return the given country.

    update:
    Update the given country.

    destroy:
    Delete the given country.
    """

    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    lookup_field = "uuid"
    http_method_names = ["get", "post", "put", "delete"]


class StateViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing states.

    create:
    Create a new state.

    retrieve:
    Return the given state.

    update:
    Update the given state.

    destroy:
    Delete the given state.
    """

    serializer_class = StateSerializer
    queryset = State.objects.all()
    permission_classes = (permissions.IsAdminUser,)
    lookup_field = "uuid"
    http_method_names = ["get", "post", "put", "delete"]

    def check_data(self, data):
        if not data:
            return Response(
                {"message": "No data provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not data.get("country"):
            return Response(
                {"message": "Country not provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not data.get("name"):
            return Response(
                {"message": "Name not provided"}, status=status.HTTP_400_BAD_REQUEST
            )

        country = Country.objects.filter(name=data.get("country"))
        if not country:
            return Response(
                {"message": "Country not found"}, status=status.HTTP_404_NOT_FOUND
            )

        state = State.objects.filter(name=data.get("name"), country=country[0])
        if state:
            return Response(
                {"message": "State already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        return country[0]

    def create(self, request, *args, **kwargs):
        country = self.check_data(request.data)
        if not isinstance(country, Country):
            return country
        State.objects.create(name=request.data.get("name"), country=country)
        return Response(
            {"message": "State created successfully"}, status=status.HTTP_201_CREATED
        )

    def update(self, request, uuid, *args, **kwargs):
        state = State.objects.filter(uuid=uuid)
        if not state:
            return Response(
                {"message": "State not found"}, status=status.HTTP_404_NOT_FOUND
            )
        country = self.check_data(request.data)
        if not isinstance(country, Country):
            return country
        state.update(name=request.data.get("name"), country=country)
        return Response(
            {"message": "State updated successfully"}, status=status.HTTP_200_OK
        )

    def destroy(self, request, uuid, *args, **kwargs):
        state = State.objects.filter(uuid=uuid)
        if not state:
            return Response(
                {"message": "State not found"}, status=status.HTTP_404_NOT_FOUND
            )
        state.delete()
        return Response(
            {"message": "State deleted successfully"}, status=status.HTTP_200_OK
        )


class CityViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing cities.

    create:
    Create a new city.

    retrieve:
    Return the given city.

    update:
    Update the given city.

    destroy:
    Delete the given city.
    """

    serializer_class = CitySerializer
    queryset = City.objects.all()
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "uuid"
    http_method_names = ["get", "post", "put", "delete"]

    def check_data(self, data):
        if not data:
            return Response(
                {"message": "No data provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not data.get("country"):
            return Response(
                {"message": "Country not provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not data.get("state"):
            return Response(
                {"message": "State not provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        if not data.get("name"):
            return Response(
                {"message": "Name not provided"}, status=status.HTTP_400_BAD_REQUEST
            )
        state = State.objects.filter(name=data.get("state"))
        if not state:
            return Response(
                {"message": "State not found"}, status=status.HTTP_404_NOT_FOUND
            )
        country = Country.objects.filter(name=data.get("country"))
        if not country:
            return Response(
                {"message": "Country not found"}, status=status.HTTP_404_NOT_FOUND
            )
        if state[0].country.name != country[0].name:
            return Response(
                {"message": "Country and State doesn't match"},
                status=status.HTTP_404_NOT_FOUND,
            )
        city = City.objects.filter(name=data.get("name"), state=state[0])
        if city:
            return Response(
                {"message": "City already exists"}, status=status.HTTP_400_BAD_REQUEST
            )
        return state[0]

    def create(self, request, *args, **kwargs):
        state = self.check_data(request.data)
        if not isinstance(state, State):
            return state
        City.objects.create(
            name=request.data.get("name"), state=state, country=state.country
        )
        return Response(
            {"message": "City created successfully"}, status=status.HTTP_201_CREATED
        )

    def update(self, request, uuid, *args, **kwargs):
        city = City.objects.filter(uuid=uuid)
        if not city:
            return Response(
                {"message": "City not found"}, status=status.HTTP_404_NOT_FOUND
            )
        state = self.check_data(request.data)
        if not isinstance(state, State):
            return state
        city.update(name=request.data.get("name"), state=state, country=state.country)
        return Response(
            {"message": "City updated successfully"}, status=status.HTTP_200_OK
        )

    def destroy(self, request, uuid, *args, **kwargs):
        city = City.objects.filter(uuid=uuid)
        if not city:
            return Response(
                {"message": "City not found"}, status=status.HTTP_404_NOT_FOUND
            )
        city.delete()
        return Response(
            {"message": "City deleted successfully"}, status=status.HTTP_200_OK
        )
