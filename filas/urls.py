"""filas URL Configuration

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
from django.contrib import admin
from django.urls import path
from core import views
from core.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    #Postos
    path('postos/', read_postos, name= "lista_postos"),
    path('create_postos/', create_postos, name= "create_postos"),
    path('update_postos/<int:id_posto>', update_postos, name= "update_postos"),
    path('delete_postos/<int:id_posto>', delete_postos, name= "delete_postos"),
    #Vacinas
    path('vacindex/', vac_index, name= "lista_vacinas"),
    path('vacreate/', vac_create, name= "create_vacinas"),
    path('vacshow/<int:id_vacina>', vac_show, name= "show_vacinas"),
    path('vacupdate/<int:id_vacina>', vac_update, name= "update_vacinas"),
    path('delete_vacinas/<int:id_vacina>', delete_vacinas, name= "delete_vacinas"),
]
