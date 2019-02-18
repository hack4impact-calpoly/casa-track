from django.contrib import admin
from .models import TrackingForm

# Register your models here.

class TrackingFormAdmin(admin.ModelAdmin):
   pass

admin.site.register(TrackingForm, TrackingFormAdmin)