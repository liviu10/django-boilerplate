from django.db import models


class Account(models.Model):
    code = models.CharField(max_length=36, default='', unique=True, null=False, blank=True)
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Accounts'


class Client(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    fiscal_code = models.CharField(max_length=12, default='', unique=True, null=True, blank=True)
    registration_number = models.CharField(max_length=20, default='', unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_name = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_account = models.CharField(max_length=32, default='', null=False, blank=True)
    phone = models.CharField(max_length=20, default='', null=False, blank=True)
    email_address = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Clients'


class Product(models.Model):
    code = models.CharField(max_length=10, default='', unique=True, null=True, blank=True)
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    sales_price = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    sales_price_with_vat = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    barcode = models.CharField(max_length=13, default='', null=False, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Products'


class Supplier(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    fiscal_code = models.CharField(max_length=12, default='', unique=True, null=True, blank=True)
    registration_number = models.CharField(max_length=20, default='', unique=True, null=True, blank=True)
    address = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_name = models.CharField(max_length=255, default='', null=False, blank=True)
    bank_account = models.CharField(max_length=32, default='', null=False, blank=True)
    phone = models.CharField(max_length=20, default='', null=False, blank=True)
    email_address = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    is_active = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Suppliers'