from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name="inicio" ),
    path('quienessomos', views.quienes_somos, name="quienes_somos" ),
    path('hola_mundo', views.hola_mundo ),
    path('saludar', views.saludar, name="saludar_por_defecto" ),
    path('saludar/<str:nombre>', views.saludar, name="saludar" ),
    path('proyectos/<int:anio>/<int:mes>', views.ver_proyectos, name="proyectos" ),
    re_path(r'^proyectos/(?P<anio>\d{2,4})/$', views.ver_proyectos_anio),
    path('proyectos/<str:nombre>/<int:numero>', views.ver_proyecto, name="proyecto" ),
    path('cursos/detalle/<slug:nombre_curso>', views.cursos_detalle, name="curso_detalle"),
    re_path(r'^cursos/(?P<nombre>\w+)/$', views.cursos, name="cursos"),
]


