from django.contrib import admin
from operations.models import *


@admin.register(CashAndBankRegister)
class CashAndBankRegisterAdmin(admin.ModelAdmin):
    model = CashAndBankRegister
    search_fields = ['document_date', 'document_number', 'is_cash_register', 'is_bank_register']
    list_display = (
        'document_date',
        'document_number',
        'document_note',
        'sum_received',
        'sum_payed',
        'is_cash_register',
        'is_bank_register'
    )


@admin.register(ConsumptionReceipt)
class ConsumptionReceiptAdmin(admin.ModelAdmin):
    model = ConsumptionReceipt
    search_fields = ['document_date', 'document_number']
    list_display = (
        'document_date',
        'document_number',
        'document_note',
        'gross_value',
        'net_value'
    )