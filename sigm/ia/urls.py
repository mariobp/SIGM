from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
import views
from .forms import CustomAuthenticationForm


urlpatterns = [
    url(r'^$', views.index , name="index"),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html',
        'authentication_form': CustomAuthenticationForm}, name='login'),
    url(r'^logout/$', views.logoutUsers, name="logOut"),
    url(r'^abrir/periodo/$', views.abrirPeriodo, name="abrir"),
    url(r'^cerrar/periodo/(?P<pk>\d+)/$', views.cerrarPeriodo, name="cerrar"),
    url(r'^registro/estudiante/$', views.registrar_e , name="registrar_e"),
    url(r'^matricula/estudiante/$', views.matricula_e , name="matricula_e"),
    url(r'^estudiante/desertados/$', views.desertados , name="desertados"),
    url(r'^lista/estudiantes/$', views.listaMatriculados , name="listaMatriculados"),
]
