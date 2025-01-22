from django.contrib import admin # type: ignore
from .models import EducationalResource,nutritonalfacts,BloodSugarReading,UserProfile

admin.site.register(UserProfile),
admin.site.register(nutritonalfacts),
admin.site.register(BloodSugarReading)
admin.site.register(EducationalResource)