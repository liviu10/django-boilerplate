from django.contrib import admin
from settings.models import *


@admin.register(AcceptedDomain)
class AcceptedDomainAdmin(admin.ModelAdmin):
    model = AcceptedDomain
    search_fields = ['domain']