from rest_framework import viewsets
from operations.serializers import *
from operations.models import *

class CashAndBankRegisterViewset(viewsets.ModelViewSet):
    queryset = CashAndBankRegister.objects.all()
    serializer_class = CashAndBankRegisterSerializer

class ConsumptionReceiptsViewset(viewsets.ModelViewSet):
    queryset = ConsumptionReceipt.objects.all()
    serializer_class = ConsumptionReceiptsSerializer
