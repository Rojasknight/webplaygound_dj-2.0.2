from django.shortcuts import render

# Vista generica: TemplateView
from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'core/home.html'

    """ Render function(traditional)"""
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'title': 'Contexto con reder'})

class SamplePageView(TemplateView):
    template_name = "core/sample.html"
