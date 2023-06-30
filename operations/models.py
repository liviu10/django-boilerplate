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
        verbose_name_plural = 'Cash and Bank Register'


class ConsumptionReceipt(models.Model):
    document_date = models.DateTimeField(max_length=36, default='', unique=True, null=False, blank=True)
    document_number = models.CharField(max_length=23, default='', unique=True, null=False, blank=True)
    document_note = models.CharField(max_length=255, default='', unique=True, null=False, blank=True)
    gross_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)
    net_value = models.DecimalField(max_digits=18, decimal_places=4, null=False, blank=True)

    class Meta:
        verbose_name_plural = 'Cash and Bank Register'