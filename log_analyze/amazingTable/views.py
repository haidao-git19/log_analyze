from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
import datetime

class jqGridDemoView(TemplateView):
    template_name = "amazingTable/base.html"
    
    def get_context_data(self, **kwargs):
        context = super(jqGridDemoView, self).get_context_data(**kwargs)
        context['time'] =  datetime.datetime.now()
        context['current_page'] = "display5"
        return context