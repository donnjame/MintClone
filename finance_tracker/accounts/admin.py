from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin
# Register your models here.



@admin.register(User)
class ViewAdmin(ImportExportModelAdmin):
    exclude = ('id', )