from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
import datetime

class HomePageView(TemplateView):
    template_name = "home/base.html"
    
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['time'] =  datetime.datetime.now()
        context['current_page'] = "home"
        return context
    