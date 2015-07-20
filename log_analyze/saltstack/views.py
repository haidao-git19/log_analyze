#!/usr/bin/env python
#coding=utf-8
#!/usr/bin/env python
#coding=utf-8
from django.views.generic.base import TemplateView
from saltapi import saltAPI
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
class SaltTestView(TemplateView):
    template_name = "saltstack/base.html"
    def get_context_data(self, **kwargs):
        context = super(SaltTestView, self).get_context_data(**kwargs)
        sapi = saltAPI()
        manage_status_param = {'client':'runner', 'fun':'manage.status'}
        test_ping_param = {'client':'local', 'fun':'test.ping', 'tgt':'*'}
        #params3 = {'client':'local', 'fun':'test.echo', 'tgt':'wwj', 'arg':'hello'}
        #grains = {'client':'local', 'fun':'grains.item', 'tgt':'ykt', 'expr_form':'nodegroup', 'arg':'os'}
        grains = {'client':'local', 'fun':'grains.item', 'arg': 'ipv4', 'tgt':'*'}
        # get the sorted json
        manage_status = sapi.saltCmd(test_ping_param)
        grains = sapi.saltCmd(grains)
    
        # render to the template
        context['manage_status'] = manage_status
        context['grains'] = grains
        context['current_page'] = "display3"
        return context

@csrf_exempt
def ajax_get_minion_statu(request):
    sapi = saltAPI()
    manage_status_param = {'client':'local', 'fun':'grains.item', 'arg': 'osfinger', 'tgt':'*'}
    manage_status = sapi.saltCmd(manage_status_param)
    return HttpResponse(manage_status, content_type='application/json')


