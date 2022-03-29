from django.db import models

from ..core.models import TimeStampedUUID


class Country(TimeStampedUUID):
    name = models.CharField("Country", max_length=60, unique=True)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class State(TimeStampedUUID):
    name = models.CharField("State", max_length=60)
    country = models.ForeignKey(
        Country,
        related_name="states",
        related_query_name="state",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"
        unique_together = ("name", "country")

    def __str__(self):
        return self.name


class City(TimeStampedUUID):
    name = models.CharField("City", max_length=60)
    country = models.ForeignKey(
        Country,
        related_name="cities",
        related_query_name="city",
        on_delete=models.CASCADE,
    )
    state = models.ForeignKey(
        State,
        related_name="cities",
        related_query_name="city",
        on_delete=models.CASCADE,
    )

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class BaseAddress(TimeStampedUUID):
    name = models.CharField("Name this address", max_length=60)
    postcode = models.CharField("Postcode", max_length=12)
    street = models.CharField("Street", max_length=100)
    apartment = models.CharField("Apartment number", max_length=4, blank=True)
    country = models.ForeignKey(
        Country,
        related_name="addresses",
        related_query_name="address",
        on_delete=models.CASCADE,
    )
    city = models.ForeignKey(
        City,
        related_name="addresses",
        related_query_name="address",
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.apartment}"
