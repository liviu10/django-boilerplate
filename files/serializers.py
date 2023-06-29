from rest_framework import serializers
from files.models import *


class AccountsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'