from rest_framework import viewsets
from files.serializers import *
from files.models import *


class AccountsViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer


class ClientsViewset(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientsSerializer


class ProductsViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductsSerializer


class SuppliersViewset(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SuppliersSerializer
