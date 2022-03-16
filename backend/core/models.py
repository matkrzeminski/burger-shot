import uuid

from django.db import models


class TimeStampedUUID(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    uuid = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Country(TimeStampedUUID):
    name = models.CharField("Country", max_length=60)

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    def __str__(self):
        return self.name


class State(TimeStampedUUID):
    country = models.ForeignKey(
        Country,
        related_name="states",
        related_query_name="state",
        on_delete=models.CASCADE,
    )
    name = models.CharField("State", max_length=60)

    class Meta:
        verbose_name = "State"
        verbose_name_plural = "States"

    def __str__(self):
        return self.name


class City(TimeStampedUUID):
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
    name = models.CharField("City", max_length=60)

    class Meta:
        verbose_name = "City"
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name


class Address(TimeStampedUUID):
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
    postcode = models.CharField("Postcode", max_length=12)
    street = models.CharField("Street", max_length=100)
    apartment = models.CharField("Apartment number", max_length=4, blank=True)

    class Meta:
        abstract = True
        verbose_name = "Address"
        verbose_name_plural = "Addresses"

    def __str__(self):
        return f"{self.street} {self.apartment}"
