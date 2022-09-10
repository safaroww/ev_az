"""evaz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path, include
from os import getenv
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import render

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path(getenv('ADMIN_URL'), admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
) + i18n_patterns(
    path('', include('sale.urls')),
    path('seller/', include('seller.urls')),
    path('info/', include('info.urls')),
)


handler404 = lambda request, exception: render(request, '404.html')