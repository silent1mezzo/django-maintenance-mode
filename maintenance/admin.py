from django.contrib import admin
from models import MaintenancePeriod

class MaintenanceAdmin(admin.ModelAdmin):
    pass

admin.site.register(MaintenancePeriod, MaintenanceAdmin)
