
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from personas import views
from personas.views import ver_persona, eliminar_persona, crear_persona, crear_automovil, editar_persona, \
    editar_automovil, ReportePersonasExcel, PersonaViewSet
from webapp.views import bienvenida

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'personas', PersonaViewSet)

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
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
