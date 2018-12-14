from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.urls import reverse, reverse_lazy
from .models import Page

# Importar vista generica 'ListView'
from django.views.generic import ListView
# Importar vista generica 'DetailView'
from django.views.generic import DetailView
# Importar vista generica 'CreateView'
from django.views.generic import CreateView
# Importar vista generica 'UpdateView' y 'DeleteView'
from django.views.generic.edit import UpdateView, DeleteView

#Modelo del formulario
from .forms import PageForm

# Create your views here.
class PagesListView(ListView):
    model = Page
    # por defecto el asigna como nombre de tamplate <pages/model_name_list.html>
    # template_name = ''


class PageDetailView(DetailView):
    model = Page
    # por defecto el asigna como nombre de tamplate <pages/model_name_list.html>
    # template_name = ''


class PageCreate(CreateView):
    model = Page
    form_class = PageForm
    #fields = ['title', 'content', 'order']
    # por defecto el asigna como nombre de tamplate <pages/model_name_list.html>
    # template_name = ''

    # def get_success_url(self):
    #    return reverse('pages:pages')

    # Redirect
    success_url = reverse_lazy('pages:pages')


class PageUpdate(UpdateView):
    model = Page
    #fields = ['title', 'content', 'order']

    form_class = PageForm

    template_name_suffix = '_update_form'

    # Es necesario sobreescribir el metodo para hacer reedirección al registro que estamos editando,
    # esto para acceder al objeto interno
    def get_success_url(self):
        #el 'ok', para validar si el registro se actualizo correctamente
        return reverse_lazy('pages:update', args=[self.object.id]) + '?ok'


class PageDelete(DeleteView):
    model = Page

    success_url = reverse_lazy('pages:pages')