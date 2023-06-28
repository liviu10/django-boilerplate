from django.db import models


class AccountType(models.Model):
    code = models.CharField(max_length=2, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Account types'


class City(models.Model):
    siruta_code = models.CharField(max_length=255, default='', null=True, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    longitude = models.CharField(max_length=255, default='', null=True, blank=True)
    latitude = models.CharField(max_length=255, default='', null=True, blank=True)
    google_maps_url = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cities'


class Company(models.Model):
    name = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    fiscal_code = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    registration_number = models.CharField(max_length=255, default='', unique=True, null=True, blank=True)
    social_capital = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'


class Country(models.Model):
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Countries'


class County(models.Model):
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Counties'


class CurrencyCode(models.Model):
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    code = models.CharField(max_length=3, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Currency codes'


class DocumentType(models.Model):
    code = models.CharField(max_length=3, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Document types'


class EconomicActivity(models.Model):
    code = models.CharField(max_length=5, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Economic activities'


class ProductType(models.Model):
    name = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Product types'


class UnitOfMeasurement(models.Model):
    code = models.CharField(max_length=5, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Unit of measurements'


class VatType(models.Model):
    code = models.CharField(max_length=6, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    value = models.IntegerField(default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Vat types'


class WarehouseType(models.Model):
    code = models.CharField(max_length=3, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    type = models.IntegerField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Warehouse types'
    