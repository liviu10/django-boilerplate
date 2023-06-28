from rest_framework import serializers
from configurations.models import *


class AccountTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccountType
        fields = '__all__'


class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class CompaniesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'


class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CountiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = County
        fields = '__all__'


class CurrencyCodesSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyCode
        fields = '__all__'


class DocumentTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocumentType
        fields = '__all__'


class EconomicActivitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = EconomicActivity
        fields = '__all__'


class ProductTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'


class UnitOfMeasurementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitOfMeasurement
        fields = '__all__'


class VatTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatType
        fields = '__all__'


class WarehouseTypesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WarehouseType
        fields = '__all__'