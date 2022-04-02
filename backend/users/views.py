from rest_framework import permissions, viewsets
from rest_framework.generics import get_object_or_404

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User, Address
from .serializers import UserSerializer, UserAddressSerializer
from ..locations.models import Country, State, City


class UserAPIView(APIView):
    """
    API endpoint that allows users to be viewed or edited.
    """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        """
        Lists all user's information includes all addresses.
        """
        user = User.objects.get(id=self.request.user.id)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class UserAddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = UserAddressSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uuid"

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        """
        Creates a new address for the user.
        """
        user = User.objects.get(id=self.request.user.id)
        if not request.data:
            return Response({"message": "No data provided"}, status=400)
        try:
            country = Country.objects.get(name=request.data.pop("country"))
        except Country.DoesNotExist:
            return Response({"error": "Country does not exist"}, status=400)
        try:
            city = country.cities.get(name=request.data.pop("city"))
        except City.DoesNotExist:
            return Response({"error": "City does not exist"}, status=400)
        request.data["country"] = country
        request.data["city"] = city
        address = Address(user=user, **request.data)
        address.save()
        serializer = UserAddressSerializer(data=address)
        if not serializer.is_valid():
            return Response(serializer.errors, status=400)
        return Response(serializer.data)




