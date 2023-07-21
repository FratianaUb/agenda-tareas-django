"""
URL configuration for poodjangocrud project.

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
from catalog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('tareas/', views.tareas, name='tareas'),
    path('tareas/listas/', views.tareas_listas, name='tareas_listas'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('Crear/tarea/', views.crear_tareas, name='crear_tareas'),
    path('tareas/<int:tarea_id>/', views.info_tarea, name='info_tarea'),
    path('tareas/<int:tarea_id>/completada', views.tareas_completadas, name='tareas_completadas'),
    path('tareas/<int:tarea_id>/eliminar', views.eliminar_tarea, name='eliminar_tarea'),
 
]
