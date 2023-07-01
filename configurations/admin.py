from django.contrib import admin
from configurations.models import *


@admin.register(AccountType)
class AccountTypeAdmin(admin.ModelAdmin):
    model = AccountType
    search_fields = ['code']
    list_display = ('code', 'name')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    model = City
    search_fields = ['name']
    list_display = ('siruta_code', 'name', 'longitude', 'latitude', 'google_maps_url')


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    model = Company
    search_fields = ['name', 'fiscal_code', 'registration_number']
    list_display = ('name', 'fiscal_code', 'registration_number', 'social_capital')


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    model = Country
    search_fields = ['name']
    list_display = ('name',)


@admin.register(County)
class CountyAdmin(admin.ModelAdmin):
    model = County
    search_fields = ['name']
    list_display = ('name',)


@admin.register(CurrencyCode)
class CurrencyCodeAdmin(admin.ModelAdmin):
    model = CurrencyCode
    search_fields = ['name', 'code']
    list_display = ('name', 'code')


@admin.register(DocumentType)
class DocumentTypeAdmin(admin.ModelAdmin):
    model = DocumentType
    search_fields = ['code', 'name']
    list_display = ('code', 'name')


@admin.register(EconomicActivity)
class EconomicActivityAdmin(admin.ModelAdmin):
    model = EconomicActivity
    search_fields = ['code', 'name']
    list_display = ('code', 'name')


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    model = ProductType
    search_fields = ['name']
    list_display = ('name',)


@admin.register(UnitOfMeasurement)
class UnitOfMeasurementAdmin(admin.ModelAdmin):
    model = UnitOfMeasurement
    search_fields = ['code', 'name']
    list_display = ('code', 'name')


@admin.register(VatType)
class VatTypeAdmin(admin.ModelAdmin):
    model = VatType
    search_fields = ['code', 'name', 'value']
    list_display = ('code', 'name', 'value')


@admin.register(WarehouseType)
class WarehouseTypeAdmin(admin.ModelAdmin):
    model = WarehouseType
    search_fields = ['code', 'name', 'type']
    list_display = ('code', 'name', 'type')