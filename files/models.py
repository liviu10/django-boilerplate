from django.db import models
from boilerplate.models import BaseModel
from configurations.models import AccountType, Country, County, City, ProductType, UnitOfMeasurement, VatType


class Account(BaseModel):
    code = models.CharField(max_length=36, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE, related_name='accounts_account_type', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Accounts'


class Client(BaseModel):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    fiscal_code = models.CharField(max_length=12, default='', unique=True, null=True, blank=True)
    registration_number = models.CharField(max_length=20, default='', unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_name = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_account = models.CharField(max_length=32, default='', null=False, blank=True)
    phone = models.CharField(max_length=20, default='', null=False, blank=True)
    email_address = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='clients_country', null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='clients_county', null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='clients_city', null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='clients_account', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Clients'


class Product(BaseModel):
    code = models.CharField(max_length=10, default='', unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    sales_price = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    sales_price_with_vat = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    barcode = models.CharField(max_length=13, default='', null=False, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='products_product_type', null=True, blank=True)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE, related_name='products_unit_of_measurement', null=True, blank=True)
    vat_type = models.ForeignKey(VatType, on_delete=models.CASCADE, related_name='products_vat_type', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'


class Supplier(BaseModel):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    fiscal_code = models.CharField(max_length=12, default='', unique=True, null=True, blank=True)
    registration_number = models.CharField(max_length=20, default='', unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_name = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_account = models.CharField(max_length=32, default='', null=False, blank=True)
    phone = models.CharField(max_length=20, default='', null=False, blank=True)
    email_address = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='suppliers_country', null=True, blank=True)
    county = models.ForeignKey(County, on_delete=models.CASCADE, related_name='suppliers_county', null=True, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='suppliers_city', null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='suppliers_account', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Suppliers'