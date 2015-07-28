
#coding:utf8
from django.shortcuts import render
from django.views.generic.base import TemplateView
# Create your views here.
import datetime
from .models import *
from django.http.response import HttpResponse
from django.core.urlresolvers import reverse_lazy
from django.views.generic.list import ListView
import json
from django.core import serializers
from rest_framework import generics
from amazingTable.serializers import ContentSerialiser


class AjaxablejqGridDemoMixin(object):
    
    def render_to_json_response(self, context, **response_kwargs):
        data = json.dumps(context)
        response_kwargs['content_type'] = 'application/json' 
        return HttpResponse(data, **response_kwargs)
    
    def form_invalid(self, form):
        print "表单不合法"
        response = super(AjaxablejqGridDemoMixin, self).form_invalid(form)
        # 如果他是ajax请求且验证未通过
        if self.request.is_ajax():
            data = {
                    'helptext': "格式不对",
                    'errors': form.errors,
            }
            return self.render_to_json_response(data, status=200)
        # 如果他不是ajax请求而且它表单验证没通过
        else:
            return response
            #return self.render_to_response(RequestContext(self.request, {'form': form}))
            #return HttpResponse("form is invalid.. this is just an HttpResponse object")
    def form_valid(self, form):
        response = super(AjaxablejqGridDemoMixin, self).form_valid(form)
        if self.request.is_ajax():
            data = {
                    'helptext': '提交成功',
            }
            return self.render_to_json_response(data, status=200)
        else:
            # return response
            return self.render_to_json_response(data, status=200)

class jqGridDemoView(AjaxablejqGridDemoMixin, ListView):
    template_name = "amazingTable/base.html"
    model = Module
    
    def get_context_data(self, **kwargs):
        context = super(jqGridDemoView, self).get_context_data(**kwargs)
        context['time'] =  datetime.datetime.now()
        context['current_page'] = "display5"
        return context

def serializerModule(request):
    queryset = Content.objects.all()
    jsons = serializers.serialize('json', queryset, use_natural_foreign_keys=True)
    if request.method == 'GET':
        return HttpResponse(jsons, content_type='application/json')
    

class ContentList(generics.ListCreateAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerialiser
    

class ContentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Content.objects.all()
    serializer_class = ContentSerialiser
    