"""
URL configuration for vila_morena_api project.

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
from rest_framework import routers
from application import views

router = routers.DefaultRouter()
router.register(r'produtos', viewset=views.ProdutoViewSet)
router.register(r'quartos', viewset=views.QuartoViewSet)
router.register(r'hospedes', viewset=views.HospedeViewSet)
router.register(r'reservas', viewset=views.ReservaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls)
]
    