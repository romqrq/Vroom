from django.contrib import admin
from .models import Car, TrackDayAddon, InsuranceAddon, PrivateDriverAddon


admin.site.register(Car)
admin.site.register(TrackDayAddon)
admin.site.register(InsuranceAddon)
admin.site.register(PrivateDriverAddon)
