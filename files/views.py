from rest_framework import viewsets
from files.serializers import *
from files.models import *

class AccountsViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountsSerializer
