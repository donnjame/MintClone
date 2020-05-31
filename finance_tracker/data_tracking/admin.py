from django.contrib import admin
from .models import MoneyAccount, Bill
from import_export.admin import ImportExportModelAdmin
# Register your models here.



@admin.register(MoneyAccount, Bill)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )