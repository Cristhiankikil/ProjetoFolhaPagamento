"""
URL configuration for projeto_django project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from crud.views import *



urlpatterns = [
    path('admin/', admin.site.urls),
    path('crud/getperson', getperson, name='get_person'),
    path('crud/addperson', addperson, name='add_person'),
    path('crud/deleteperson/<int:person_id>', deleteperson, name='delete_person'),
    path('crud/editPerson', editPerson, name='edit_person'),
   
    path('crud/getEmpresa', getEmpresa, name='get_empresa'),
    path('crud/addEmpresa', addEmpresa, name='add_empresa'),
    path('crud/deleteEmpresa/<int:empresa_id>', deleteempresa, name='delete_empresa'),
    path('crud/editEmpresa', editEmpresa, name='edit_empresa'),
]
