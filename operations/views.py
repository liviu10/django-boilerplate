from rest_framework import viewsets
from operations.serializers import *
from operations.models import *


class CashAndBankRegisterViewset(viewsets.ModelViewSet):
    queryset = CashAndBankRegister.objects.all()
    serializer_class = CashAndBankRegisterSerializer


class InvoicesViewset(viewsets.ModelViewSet):
    queryset = Invoice.objects.all()
    serializer_class = InvoicesSerializer


class ConsumptionReceiptsViewset(viewsets.ModelViewSet):
    queryset = ConsumptionReceipt.objects.all()
    serializer_class = ConsumptionReceiptsSerializer


class InvoiceLinesViewset(viewsets.ModelViewSet):
    queryset = InvoiceLine.objects.all()
    serializer_class = InvoiceLinesSerializer


class ConsumptionReceiptLinesViewset(viewsets.ModelViewSet):
    queryset = ConsumptionReceiptLine.objects.all()
    serializer_class = ConsumptionReceiptLinesSerializer


class SalesInvoicesViewset(viewsets.ModelViewSet):
    queryset = SalesInvoice.objects.all()
    serializer_class = SalesInvoicesSerializer


class ShippingNotesViewset(viewsets.ModelViewSet):
    queryset = ShippingNote.objects.all()
    serializer_class = ShippingNotesSerializer


class SalesInvoiceLinesViewset(viewsets.ModelViewSet):
    queryset = SalesInvoiceLine.objects.all()
    serializer_class = SalesInvoiceLinesSerializer


class ShippingNoteLinesViewset(viewsets.ModelViewSet):
    queryset = ShippingNoteLine.objects.all()
    serializer_class = ShippingNoteLinesSerializer
