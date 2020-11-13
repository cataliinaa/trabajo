from django.urls import path, include
from . import views
from .views import RegistroUsuario, UserList


urlpatterns = [
    path('Registrar', RegistroUsuario.as_view(), name="Registrar"),
    path('List_user', UserList.as_view(), name="List_user"),
]
