from django.db import models
from boilerplate.models import BaseModel


class AccountType(BaseModel):
    code = models.CharField(max_length=2, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Account types'


class Country(BaseModel):
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Countries'


class County(BaseModel):
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='counties_country', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Counties'


class City(BaseModel):
    siruta_code = models.CharField(max_length=255, default='', null=True, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    longitude = models.CharField(max_length=255, default='', null=True, blank=True)
    latitude = models.CharField(max_length=255, default='', null=True, blank=True)
    google_maps_url = models.CharField(max_length=255, default='', null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='cities_county', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cities'


class CurrencyCode(BaseModel):
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    code = models.CharField(max_length=3, default='', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='currency_codes_country', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Currency codes'


class DocumentType(BaseModel):
    code = models.CharField(max_length=3, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Document types'


class EconomicActivity(BaseModel):
    code = models.CharField(max_length=5, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Economic activities'


class Company(BaseModel):
    name = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    fiscal_code = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    registration_number = models.CharField(max_length=255, default='', unique=True, null=True, blank=True)
    social_capital = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    economic_activity = models.ForeignKey(EconomicActivity, on_delete=models.CASCADE, related_name='companies_economic_activity', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Companies'


class CompanyDetails(BaseModel):
    address = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_name = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_account = models.CharField(max_length=32, default='', null=False, blank=True)
    phone = models.CharField(max_length=20, default='', null=False, blank=True)
    email_address = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_details_company', null=True, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='company_details_country', null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='company_details_county', null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='company_details_city', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Company details'


class CompanySettings(BaseModel):
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='company_settings_company', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Company settings'


class ProductType(BaseModel):
    name = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)

    class Meta:
        verbose_name = 'Product type'


class UnitOfMeasurement(BaseModel):
    code = models.CharField(max_length=5, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Unit of measurements'


class VatType(BaseModel):
    code = models.CharField(max_length=6, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    value = models.IntegerField(default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Vat types'


class WarehouseType(BaseModel):
    code = models.CharField(max_length=3, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=True, blank=True)
    type = models.IntegerField(default='', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Warehouse types'
    