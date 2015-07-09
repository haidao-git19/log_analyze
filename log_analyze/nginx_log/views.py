#coding: utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
import datetime
    
class DisplayOneView(TemplateView):
    template_name = "nginx_log/base.html"
    
    def get_context_data(self, **kwargs):
        context = super(DisplayOneView, self).get_context_data(**kwargs)
        context['time'] =  datetime.datetime.now()
        context['current_page'] = "display1"
        return context

class DisplayTwoView(TemplateView):
    template_name = "nginx_log/another.html"
    
    def get_context_data(self, **kwargs):
        context = super(DisplayTwoView, self).get_context_data(**kwargs)
        
        # 查找日志
        path="/Users/kevin/Documents/workspace/log_analyze/pretreatment.log"
        data = {}
        
        # 读取日志
        with open(path) as f:
            for line in f:
                line.strip()
                
                # 处理精简日志
                country, temperature = line.split(':')
                data[country] = temperature
                
        context['path'] = path
        context['countryAndTemperature'] = data
        context['time'] =  datetime.datetime.now()
        context['current_page'] = "display2"
        return context
    
