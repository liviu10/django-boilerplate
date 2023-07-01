from rest_framework import viewsets
from operations.serializers import *
from operations.models import *


class CashAndBankRegisterViewset(viewsets.ModelViewSet):
    queryset = CashAndBankRegister.objects.all()
    serializer_class = CashAndBankRegisterSerializer


class ConsumptionReceiptsViewset(viewsets.ModelViewSet):
    queryset = ConsumptionReceipt.objects.all()
    serializer_class = ConsumptionReceiptsSerializer


class ConsumptionReceiptLinesViewset(viewsets.ModelViewSet):
    queryset = ConsumptionReceiptLine.objects.all()
    serializer_class = ConsumptionReceiptLinesSerializer


class InvoicesViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoicesSerializer


class InvoiceLinesViewset(viewsets.ModelViewSet):
    queryset = InvoiceLine.objects.all()
    serializer_class = InvoiceLinesSerializer


class SalesInvoicesViewset(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoicesSerializer


class SalesInvoiceLinesViewset(viewsets.ModelViewSet):
    queryset = SalesInvoiceLine.objects.all()
    serializer_class = SalesInvoiceLinesSerializer


class ShippingNotesViewset(viewsets.ModelViewSet):
    queryset = ShippingNote.objects.all()
    serializer_class = ShippingNotesSerializer


class ShippingNoteLinesViewset(viewsets.ModelViewSet):
    queryset = ShippingNoteLine.objects.all()
    serializer_class = ShippingNoteLinesSerializer
