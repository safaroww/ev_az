from django.contrib import admin
from .models import (
    City, PropertyType, PurchaseType,
    Property, PropertyFeature, PorpertyImage
)

# Register your models here.
admin.site.register(City)
admin.site.register(PropertyType)
admin.site.register(PurchaseType)
admin.site.register(PropertyFeature)


class PropertyImageInline(admin.TabularInline):
    model = PorpertyImage
    
@admin.register(Property)
class PorpertyAdmin(admin.ModelAdmin):
    exclude = ['update', 'created']
    inlines = [PropertyImageInline]
