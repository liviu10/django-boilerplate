"""
URL configuration for boilerplate project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

configurations_urlpatterns = [
    path('configurations/', include('configurations.urls')),
]

files_urlpatterns = [
    path('files/', include('files.urls')),
]

operations_urlpatterns = [
    path('operations/', include('operations.urls')),
]

settings_urlpatterns = [
    path('settings/', include('settings.urls')),
]

urlpatterns = [
    path('', RedirectView.as_view(url='/admin/')),
    path('admin/', admin.site.urls),
] + configurations_urlpatterns + files_urlpatterns + operations_urlpatterns + settings_urlpatterns
