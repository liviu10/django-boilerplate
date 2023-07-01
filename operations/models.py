from django.db import models
from boilerplate.models import BaseModel
from configurations.models import DocumentType, ProductType, UnitOfMeasurement, VatType, WarehouseType
from files.models import Account, Client, Product, Supplier

IS_CASH_AND_BANK_REGISTER_CHOICES = [(False, 'No'), (True, 'Yes')]
IS_ELECTRONIC_INVOICE_CHOICES = [(False, 'No'), (True, 'Yes')]
IS_VAT_CASH_ON_RECEIVED_CHOICES = [(False, 'No'), (True, 'Yes')]

class CashAndBankRegister(BaseModel):
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    document_note = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    sum_received = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    sum_payed = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    is_cash_register = models.BooleanField(default=False, null=True, blank=True, choices=IS_CASH_AND_BANK_REGISTER_CHOICES)
    is_bank_register = models.BooleanField(default=False, null=True, blank=True, choices=IS_CASH_AND_BANK_REGISTER_CHOICES)

    class Meta:
        verbose_name_plural = 'Cash and bank register'


class Invoice(BaseModel):
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    vat_on_cash_received = models.BooleanField(default=False, null=True, blank=True, choices=IS_VAT_CASH_ON_RECEIVED_CHOICES)
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_due_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name='invoices_document_type', null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='invoices_supplier', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Invoices'


class ConsumptionReceipt(BaseModel):
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    document_note = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name='consumption_receipts_document_type', null=True, blank=True)
    invoice = models.OneToOneField(Invoice, on_delete=models.CASCADE, related_name='consumption_receipts_invoice', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Consumption receipts'


class InvoiceLine(BaseModel):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    discount = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='invoice_lines_product_type', null=True, blank=True)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE, related_name='invoice_lines_unit_of_measurement', null=True, blank=True)
    vat_type = models.ForeignKey(VatType, on_delete=models.CASCADE, related_name='invoice_lines_vat_type', null=True, blank=True)
    warehouse_type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE, related_name='invoice_lines_warehouse_type', null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='invoice_lines_account', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='invoice_lines_product', null=True, blank=True)
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE, related_name='invoice_lines_invoice', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Invoice lines'


class ConsumptionReceiptLine(BaseModel):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_type = models.ForeignKey(VatType, on_delete=models.CASCADE, related_name='consumption_receipt_lines_vat_type', null=True, blank=True)
    warehouse_type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE, related_name='consumption_receipt_lines_warehouse_type', null=True, blank=True)
    consumption_receipt = models.ForeignKey(ConsumptionReceipt, on_delete=models.CASCADE, related_name='consumption_receipt_lines_consumption_receipt', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Consumption receipt lines'


class SalesInvoice(BaseModel):
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    electronic_invoice = models.BooleanField(default=False, null=True, blank=True, choices=IS_ELECTRONIC_INVOICE_CHOICES)
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_due_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name='sales_invoices_document_type', null=True, blank=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales_invoices_client', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Sales invoices'


class SalesInvoiceLine(BaseModel):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    discount = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    product_type = models.ForeignKey(ProductType, on_delete=models.CASCADE, related_name='sales_invoice_lines_product_type', null=True, blank=True)
    unit_of_measurement = models.ForeignKey(UnitOfMeasurement, on_delete=models.CASCADE, related_name='sales_invoice_lines_unit_of_measurement', null=True, blank=True)
    vat_type = models.ForeignKey(VatType, on_delete=models.CASCADE, related_name='sales_invoice_lines_vat_type', null=True, blank=True)
    warehouse_type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE, related_name='sales_invoice_lines_warehouse_type', null=True, blank=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='sales_invoice_lines_account', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='sales_invoice_lines_product', null=True, blank=True)
    sales_invoice = models.ForeignKey(SalesInvoice, on_delete=models.CASCADE, related_name='sales_invoice_lines_sales_invoice', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Sales invoice lines'


class ShippingNote(BaseModel):
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    document_note = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    document_type = models.ForeignKey(DocumentType, on_delete=models.CASCADE, related_name='shipping_notes_document_type', null=True, blank=True)
    sales_invoice = models.OneToOneField(SalesInvoice, on_delete=models.CASCADE, related_name='shipping_notes_sales_invoice', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Shipping notes'


class ShippingNoteLine(BaseModel):
    name = models.CharField(max_length=255, default='', null=False, blank=True)
    quantity = models.IntegerField(null=False, blank=True)
    unit_gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_amount_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    unit_net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    vat_type = models.ForeignKey(VatType, on_delete=models.CASCADE, related_name='shipping_note_lines_vat_type', null=True, blank=True)
    warehouse_type = models.ForeignKey(WarehouseType, on_delete=models.CASCADE, related_name='shipping_note_lines_warehouse_type', null=True, blank=True)
    shipping_note = models.ForeignKey(ShippingNote, on_delete=models.CASCADE, related_name='shipping_note_lines_sales_invoice', null=True, blank=True)

    class Meta:
        verbose_name_plural = 'Shipping note lines'