from rest_framework import permissions
from rest_framework.generics import ListAPIView

from .models import Country
from .serializers import CountrySerializer


class CountryListAPIView(ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_classes = [permissions.IsAuthenticated]
