from rest_framework import serializers
from settings.models import *


class AcceptedDOmainsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AcceptedDomain
        fields = '__all__'