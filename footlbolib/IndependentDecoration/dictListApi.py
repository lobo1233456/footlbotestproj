# -*- coding: GBK -*-

import time
import json
import requests
import settings


urlBase= settings.URlBASE
class DictInfo():
    def __init__(self,accountName='liubo',password='123456'):
        self.accountName  =accountName
        self.password =password

    def urlBasefun(self):
        return urlBase
    def _keepSession(self):
        url = urlBase + "ms/check_login.do"
        payload = {
            "accountName": "%s"%self.accountName,
            "checkCode": "",
            "password": "%s"%self.password
        }
        headers = {
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        return response.headers['Set-Cookie']
    def nameRandom(self):
        time.sleep(0.1)
        return "test" + str(round(time.time(),1))
    def creatID(self,newName):
        '''
           Id���������
        :param newName:
        :return:
        '''
        url = DictInfo().urlBasefun() +"ms/custom/dict/save.do"
        payload = {
                "redirect": "",
                "dictId": "",
                "dictName": "%s"%newName,
                "dictValue": "1",
                "dictSort": "2",
                "dictDescription": "3",
                "groupIds": "19,1017"
            }
            
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self):
        '''
            ����ͨ��dictName������������ʽparams
        :return:
        '''
        url = DictInfo().urlBasefun() +"ms/custom/dict/list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%DictInfo()._keepSession(),
        }
        response = requests.request("GET", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,appId,newName):
        url = DictInfo().urlBasefun() +"ms/custom/dict/update.do"
        payload = {
            "redirect": "",
            "dictId": appId,
            "dictName": "%s"%newName,
            "dictValue": "1",
            "dictSort": "2",
            "dictDescription": "3",
            "groupIds": "19,1017"
        }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%DictInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response)
    def delete(self,id):
        url = DictInfo().urlBasefun() +"ms/custom/dict/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%DictInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)

        return(response.text)

    def AccurateSearch(self, id):
        url = DictInfo().urlBasefun() + "ms/custom/dict/info/%s.do" % id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % DictInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return  response

