from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Vahaan,VahaanClasses,VahaanServices,VahaanServiesTracker,Sarthi,SarthiServices,SarthiClasses,SarthiServiesTracker
# Register your models here.
@admin.register(Vahaan)
class VahaanAdmin(ImportExportModelAdmin):
    pass

@admin.register(VahaanClasses)
class VahaanClassesAdmin(ImportExportModelAdmin):
    pass

@admin.register(VahaanServices)
class VahaanServicesAdmin(ImportExportModelAdmin):
    pass

@admin.register(VahaanServiesTracker)
class VahaanServiesTrackerAdmin(ImportExportModelAdmin):
    pass

@admin.register(Sarthi)
class SarthiAdmin(ImportExportModelAdmin):
    pass

@admin.register(SarthiServices)
class SarthiServicesAdmin(ImportExportModelAdmin):
    pass

@admin.register(SarthiClasses)
class SarthiClassesAdmin(ImportExportModelAdmin):
    pass

@admin.register(SarthiServiesTracker)
class SarthiServiesTrackerAdmin(ImportExportModelAdmin):
    pass