from django.contrib import admin

# Register your models here.
from django.contrib import admin

# Register your models here.
from .models import Sensor, Measurement

class MeasurementInline(admin.TabularInline):
    model = Measurement
    list_display = ['id', 'temperature', 'date']
    extra = 1

@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'description']
    inlines = [
        MeasurementInline,
    ]

@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id','temperature', 'date']


