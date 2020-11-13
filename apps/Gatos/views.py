from django.shortcuts import render
from . import views
from .forms import Gatos_en_adopcion_form
from .models import Gatos_en_adopcion,Usuario
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from django.db.models import Q 

# Crud
class Gatos_en_adopcion_Create(CreateView):
    model = Gatos_en_adopcion
    form_class = Gatos_en_adopcion_form
    template_name = 'Gatos/Añadir_gato.html'
    success_url = reverse_lazy("Listar_gato/")

class Gatos_en_adopcion_List(ListView):
    model = Gatos_en_adopcion
    template_name = 'Gatos/Listar_gato.html'
    # paginate_by = 4

class Gatos_en_adopcion_Update(UpdateView):
    model = Gatos_en_adopcion
    form_class = Gatos_en_adopcion_form
    template_name = 'Gatos/Editar_gato.html'
    success_url = reverse_lazy('Listar_gato/')
    
class Gatos_en_adopcion_Delete(DeleteView):
    model = Gatos_en_adopcion
    template_name = 'Gatos/Eliminar_gato.html'
    success_url = reverse_lazy('Listar_gato/')
 

#busqueda
class Buscar_gatos_view(ListView):
    model = Gatos_en_adopcion
    template_name = 'Gatos/Buscar_gatos.html'

class SearchResultsView(ListView):
    model =Gatos_en_adopcion
    template_name = 'Gatos/search_results.html'
    
    def get_queryset(self): 
        query = self.request.GET.get('q')
        object_list = Gatos_en_adopcion.objects.filter(
            Q(raza__icontains=query) )
        return object_list


def ver_gatos(request):
    gatos = Gatos_en_adopcion.objects.all()
    return render(request, "Gatos/Listar_gato2.html", {'gatos': gatos})