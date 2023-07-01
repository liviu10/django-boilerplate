from rest_framework import viewsets
from settings.serializers import *
from settings.models import *


class AcceptedDomainsViewset(viewsets.ModelViewSet):
    queryset = AcceptedDomain.objects.all()
    serializer_class = AcceptedDomainsSerializer


class ErrorsAndNotificationsViewset(viewsets.ModelViewSet):
    queryset = ErrorAndNotification.objects.all()
    serializer_class = ErrorsAndNotificationsSerializer
