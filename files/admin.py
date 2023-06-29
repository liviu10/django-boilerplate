from django.contrib import admin
from files.models import *


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    model = Account
    search_fields = ['code', 'name', 'is_active']
    list_display = ('code', 'name', 'is_active')