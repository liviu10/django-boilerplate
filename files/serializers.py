from rest_framework import serializers
from files.models import *


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'


class ClientsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class SuppliersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'