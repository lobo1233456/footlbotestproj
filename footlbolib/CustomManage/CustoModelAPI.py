# -*- coding: GBK -*-
import time
import json
import requests
import settings

urlBase= settings.URlBASE
class modelInfo():
    def __init__(self,accountName='admin',password='123456'):
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
            appId会随机生成
        :param newName:
        :return:
        '''
        url = modelInfo().urlBasefun() +"ms/custom/content_model/save.do"
        payload = {
            "redirect": "", "modelId": "", "modelCode": "%s"%newName, "modelName": "%s"%newName, "modelDescription": "3"
        }



        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self):
        url = modelInfo().urlBasefun() +"ms/custom/content_model/list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,modelId,newName):
        url = modelInfo().urlBasefun() +"ms/custom/content_model/update.do"
        payload = {
            "redirect": "", "modelId": modelId, "modelCode": "1", "modelName": "%s"%newName, "modelDescription": "3"
        }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        # response = json.loads(response.text)
        return(response)
    def delete(self,id):
        '''
            http://csf.91clt.com:8090/fycms/ms/custom/content_model/delete.do
        :param id:
        :return:
        '''
        url = modelInfo().urlBasefun() +"ms/custom/content_model/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)

    def AccurateSearch(self, id):
        url = modelInfo().urlBasefun() + "ms/custom/content_model/info/%s.do" % id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % modelInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return  response





