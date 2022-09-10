from django.urls import path
from . import views

app_name = 'sale'

urlpatterns = [
    path('', views.home, name='home'),
    path('property-list/', views.property_list, name='property-list'),
    path('property-detail/', views.property_detail, name='property-detail'),
]