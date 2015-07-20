#!/usr/bin/env python
#_*_coding:utf-8_*_

import urllib2, urllib, json, re

class saltAPI:
    def __init__(self):
        self.__url = 'http://10.211.55.5:8000'       #salt-api监控的地址和端口如:'http://192.168.46.185:8888'
        self.__user =  'gaoyuan'             #salt-api用户名
        self.__password = 'gaoyuan'          #salt-api用户密码
        self.__token_id = self.salt_login()

    def salt_login(self):
        params = {
                'eauth': 'pam', 'username': self.__user, 'password': self.__password}
        encode = urllib.urlencode(params)
        obj = urllib.unquote(encode)
        headers = {'X-Auth-Token':''}
        url = self.__url + '/login'
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        try:
            token = content['return'][0]['token']
            return token
        except KeyError:
            raise KeyError

    def postRequest(self, obj, prefix='/'):
        url = self.__url + prefix
        headers = {'X-Auth-Token'   : self.__token_id}
        req = urllib2.Request(url, obj, headers)
        opener = urllib2.urlopen(req)
        content = json.loads(opener.read())
        return content['return']

    def saltCmd(self, params):
        obj = urllib.urlencode(params)
        obj, number = re.subn("arg\d", 'arg', obj)
        res = self.postRequest(obj)
        # sort it
        res = json.dumps(res, sort_keys=True)
        return res
    
def main():
    #以下是用来测试saltAPI类的部分
    sapi = saltAPI()
    params = {'client':'local', 'fun':'test.ping', 'tgt':'*'}
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'wwj'}
    #params = {'client':'local', 'fun':'test.echo', 'tgt':'某台服务器的key', 'arg1':'hello'}
    #params = {'client':'local', 'fun':'test.ping', 'tgt':'ykt', 'expr_form':'nodegroup'}
    test = sapi.saltCmd(params)
    print test

if __name__ == '__main__':
    main()