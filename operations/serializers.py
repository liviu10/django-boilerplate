from rest_framework import serializers
from operations.models import *


class CashAndBankRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CashAndBankRegister
        fields = '__all__'


class ConsumptionReceiptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumptionReceipt
        fields = '__all__'