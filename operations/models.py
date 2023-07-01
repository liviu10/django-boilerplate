from django.db import models


class CashAndBankRegister(models.Model):
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    document_note = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    sum_received = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    sum_payed = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    is_cash_register = models.BooleanField(default=False, null=True, blank=True)
    is_bank_register = models.BooleanField(default=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Cash and bank register'


class ConsumptionReceipt(models.Model):
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    document_note = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Consumption receipts'


class ConsumptionReceiptLine(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Consumption receipt lines'


class Invoice(models.Model):
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    vat_on_cash_received = models.BooleanField(default=False, null=True, blank=True)
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_due_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Invoices'


class InvoiceLine(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    discount = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Invoice lines'


class SalesInvoice(models.Model):
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    electronic_invoice = models.BooleanField(default=False, null=True, blank=True)
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_due_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Sales invoices'


class SalesInvoiceLine(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    discount = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Sales invoice lines'


class ShippingNote(models.Model):
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    document_note = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Shipping notes'


class ShippingNoteLine(models.Model):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Shipping note lines'