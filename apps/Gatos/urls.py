from django.urls import path, include
from . import views
from .forms import Gatos_en_adopcion_form
from .views import Buscar_gatos_view , SearchResultsView
from django.contrib.auth.views import login_required

urlpatterns= [
    path('Añadir_gato', login_required(views.Gatos_en_adopcion_Create.as_view()), name="Añadir_gato"),

    path('Listar_gato/', views.Gatos_en_adopcion_List.as_view(), name='Listar_gato/'),

    path('Editar_gato/<int:pk>', login_required(views.Gatos_en_adopcion_Update.as_view()), name='Editar_gato'),

    path('Eliminar_gato/<int:pk>', login_required(views.Gatos_en_adopcion_Delete.as_view()), name='Eliminar_gato'),

     path('Buscar_gatos/', Buscar_gatos_view.as_view(), name='Buscar_gatos/'),

     path('search/', SearchResultsView.as_view(), name='search/'),

     path('Listar_gato2/', views.ver_gatos, name='Listar_gato2/'),

]