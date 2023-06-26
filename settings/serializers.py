from rest_framework import serializers
from settings.models import *


class AcceptedDomainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedDomain
        fields = '__all__'


class ErrorsAndNotificationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ErrorAndNotification
        fields = '__all__'