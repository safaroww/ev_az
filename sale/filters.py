import django_filters as filters
from .models import Property, City, PropertyType, PurchaseType
from django import forms
from django.db import models

class PropertyFilter(filters.FilterSet):
    
    price = filters.NumericRangeFilter('price', 'range')
    city = filters.ModelChoiceFilter(queryset=City.objects.all(), empty_label='Hamısı')
    type = filters.ModelChoiceFilter(queryset=PropertyType.objects.all(), empty_label='Hamısı')
    purchase = filters.ModelChoiceFilter(queryset=PurchaseType.objects.all(), empty_label='Hamısı')
    class Meta:
        model = Property
        fields = ['city', 'type', 'purchase', 'new', 'repaired']
        # filter_overrides = {
        #     models.BooleanField: {
        #         'filter_class': filters.BooleanFilter,
        #         'extra': lambda f: {
        #             'widget': forms.CheckboxInput,
        #         },
        #     }
        # }