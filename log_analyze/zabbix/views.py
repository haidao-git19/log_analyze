from django.shortcuts import render

# Create your views here.
import json
import urllib2
from django.views.generic.base import TemplateView

# based url and required header
url = "http://10.211.55.5/zabbix/api_jsonrpc.php"
header = {
        "Content-Type": "application/json",
}

# auth user and pwd
data_auth = json.dumps(
{
        "jsonrpc": "2.0",
        "method": "user.login",
        "params": {
                "user": "Admin",
                "password": "zabbix"
        },
"id": 0
})



# auth and get authid
def login():
    # create request object
    request = urllib2.Request(url, data_auth)
    for key in header:
            request.add_header(key, header[key])
    try:
        result = urllib2.urlopen(request)
    except urllib2.URLError as e:
        print "Auth Failed, Please Check Your Name And Password:", e.code
    else:
        response = json.loads(result.read())
        result.close()
    return response['result']

data_history = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "history.get",
    "params": {
        "history":0,
        "itemids":["23735"],
        "output":"extend"
    },
    "auth": login(),
    "id": 1
})

def get_history():
    # create request object
    request = urllib2.Request(url, data_history)
    for key in header:
            request.add_header(key, header[key])
    try:
        result = urllib2.urlopen(request)
    except urllib2.URLError as e:
        print "Failed, Please Check Your Name And Password:", e.code
    else:
        response = json.loads(result.read())
        print response['result'][1]['value']
        result.close()
    return response['result']
    
class ZabbixDemoView(TemplateView):
    template_name = "zabbix/base.html"
    
    def get_context_data(self, **kwargs):
        context = super(ZabbixDemoView, self).get_context_data(**kwargs)
        context['token'] = login()
        context['history'] = get_history()
        context['current_page'] = "display4"
        return context