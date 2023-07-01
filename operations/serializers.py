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


class ConsumptionReceiptLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConsumptionReceiptLine
        fields = '__all__'


class InvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = '__all__'


class InvoiceLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceLine
        fields = '__all__'


class SalesInvoicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoice
        fields = '__all__'


class SalesInvoiceLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = SalesInvoiceLine
        fields = '__all__'


class ShippingNotesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingNote
        fields = '__all__'


class ShippingNoteLinesSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingNoteLine
        fields = '__all__'