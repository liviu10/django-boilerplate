from django.contrib import admin
from files.models import *


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account
    search_fields = ['code', 'name', 'is_active']
    list_display = ('code', 'name', 'is_active')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    model = Client
    search_fields = ['name', 'fiscal_code', 'registration_number', 'is_active']
    list_display = (
        'name',
        'fiscal_code',
        'registration_number',
        'address',
        'bank_name',
        'bank_account',
        'phone',
        'email_address',
        'is_active'
    )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    model = Product
    search_fields = ['code', 'name', 'is_active']
    list_display = (
        'code',
        'name',
        'sales_price',
        'sales_price_with_vat',
        'barcode',
        'is_active'
    )


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    model = Supplier
    search_fields = ['name', 'fiscal_code', 'registration_number', 'is_active']
    list_display = (
        'name',
        'fiscal_code',
        'registration_number',
        'address',
        'bank_name',
        'bank_account',
        'phone',
        'email_address',
        'is_active'
    )