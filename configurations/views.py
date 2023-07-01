from rest_framework import viewsets
from configurations.serializers import *
from configurations.models import *


class AccountTypesViewset(viewsets.ModelViewSet):
    queryset = AccountType.objects.all()
    serializer_class = AccountTypesSerializer


class CountriesViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountriesSerializer


class CountiesViewset(viewsets.ModelViewSet):
    queryset = County.objects.all()
    serializer_class = CountiesSerializer


class CitiesViewset(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitiesSerializer


class CurrencyCodesViewset(viewsets.ModelViewSet):
    queryset = CurrencyCode.objects.all()
    serializer_class = CurrencyCodesSerializer


class DocumentTypesViewset(viewsets.ModelViewSet):
    queryset = DocumentType.objects.all()
    serializer_class = DocumentTypesSerializer


class EconomicActivitiesViewset(viewsets.ModelViewSet):
    queryset = EconomicActivity.objects.all()
    serializer_class = EconomicActivitiesSerializer


class CompaniesViewset(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompaniesSerializer


class CompanyDetailsViewset(viewsets.ModelViewSet):
    queryset = CompanyDetails.objects.all()
    serializer_class = CompanyDetailsSerializer


class CompanySettingsViewset(viewsets.ModelViewSet):
    queryset = CompanySettings.objects.all()
    serializer_class = CompanySettingsSerializer


class ProductTypesViewset(viewsets.ModelViewSet):
    queryset = ProductType.objects.all()
    serializer_class = ProductTypesSerializer


class UnitOfMeasurementsViewset(viewsets.ModelViewSet):
    queryset = UnitOfMeasurement.objects.all()
    serializer_class = UnitOfMeasurementsSerializer


class VatTypesViewset(viewsets.ModelViewSet):
    queryset = VatType.objects.all()
    serializer_class = VatTypesSerializer


class WarehouseTypesViewset(viewsets.ModelViewSet):
    queryset = WarehouseType.objects.all()
    serializer_class = WarehouseTypesSerializer
