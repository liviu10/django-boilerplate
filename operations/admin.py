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


@admin.register(Invoice)
class InvoicesAdmin(admin.ModelAdmin):
    model = Invoice
    search_fields = ['document_number', 'document_date', 'document_due_date']
    list_display = (
        'document_number',
        'vat_on_cash_received',
        'document_date',
        'document_due_date',
        'gross_value',
        'net_value'
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


@admin.register(InvoiceLine)
class InvoiceLinesAdmin(admin.ModelAdmin):
    model = InvoiceLine
    search_fields = ['name']
    list_display = (
        'name',
        'quantity',
        'unit_gross_value',
        'discount',
        'vat_amount_value',
        'unit_net_value'
    )


@admin.register(ConsumptionReceiptLine)
class ConsumptionReceiptLinesAdmin(admin.ModelAdmin):
    model = ConsumptionReceiptLine
    search_fields = ['name']
    list_display = (
        'name',
        'quantity',
        'unit_gross_value',
        'vat_amount_value',
        'unit_net_value'
    )


@admin.register(SalesInvoice)
class SalesInvoicesAdmin(admin.ModelAdmin):
    model = SalesInvoice
    search_fields = ['document_number', 'document_date', 'document_due_date']
    list_display = (
        'document_number',
        'electronic_invoice',
        'document_date',
        'document_due_date',
        'gross_value',
        'net_value'
    )


@admin.register(ShippingNote)
class ShippingNotesAdmin(admin.ModelAdmin):
    model = SalesInvoice
    search_fields = ['document_number', 'document_date']
    list_display = (
        'document_number',
        'document_date',
        'gross_value',
        'net_value',
        'document_note'
    )


@admin.register(SalesInvoiceLine)
class SalesInvoiceLinesAdmin(admin.ModelAdmin):
    model = SalesInvoiceLine
    search_fields = ['name']
    list_display = (
        'name',
        'quantity',
        'unit_gross_value',
        'discount',
        'vat_amount_value',
        'unit_net_value'
    )


@admin.register(ShippingNoteLine)
class ShippingNoteLinesAdmin(admin.ModelAdmin):
    model = ShippingNoteLine
    search_fields = ['name']
    list_display = (
        'name',
        'quantity',
        'unit_gross_value',
        'vat_amount_value',
        'unit_net_value'
    )