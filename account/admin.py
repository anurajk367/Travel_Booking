from django.contrib import admin
from .models import Packages,TravelItinerary,Event
from django.forms.widgets import TextInput
from django.db import models
from django import forms




class ItineraryInline(admin.TabularInline):  # Use TabularInline for a table-like display

    model = TravelItinerary

class PackageAdmin(admin.ModelAdmin):
    # Your Package admin customization
    inlines = [ItineraryInline]  # Associate the ItineraryInline with PackageAdmin




# Register both models and their admin classes
admin.site.register(Packages, PackageAdmin)
admin.site.register(TravelItinerary)
admin.site.register(Event)