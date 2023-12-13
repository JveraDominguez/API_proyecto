"""
URL configuration for sap project.

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
from django.urls import path

from personas.views import ver_persona, eliminar_persona, crear_persona, crear_automovil, editar_persona, \
    editar_automovil, ReportePersonasExcel
from webapp.views import bienvenida

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',bienvenida,name='inicio'),
    path('ver_persona/<int:persona_id>/', ver_persona, name='ver_persona'),
    path('eliminar_persona/<int:persona_id>/', eliminar_persona, name='eliminar_persona'),
    path('crear_persona/', crear_persona, name='crear_persona'),
    path('crear_automovil/', crear_automovil, name='crear_automovil'),
    path('editar_persona/<int:persona_id>/', editar_persona, name='editar_persona'),
    path('editar_automovil/<int:automovil_id>/', editar_automovil, name='editar_automovil'),
    path('reporte_excel/', ReportePersonasExcel.as_view(),name='reporte'),
]
