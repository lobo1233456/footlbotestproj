# -*- coding: GBK -*-
import time
import json
import requests
import settings

urlBase= settings.URlBASE
class modeladInfo():
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
            appId会随机生成
        :param newName:
        :return:
        '''
        url = modeladverInfo().urlBasefun() +"ms/cms/ad_position/save.do"
        payload = {
            "redirect": "",
            "id": "",
            "positionName": "test",
            "code": "%s"%newName,
            "positionType": "0",
            "description": "测测测，劢軧錒慪黑稿"
        }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self):
        url = modeladverInfo().urlBasefun() +"ms/cms/ad_position/list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modeladverInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,modelId,newName):
        url = modeladverInfo().urlBasefun() +"ms/cms/ad_position/update.do"
        payload = {
            "redirect": "",
            "id": "%s"%modelId,
            "positionName": "test",
            "code": "%s"%newName,
            "positionType": "0",
            "description": "测测测，劢軧錒慪黑稿"
        }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modeladverInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        # response = json.loads(response.text)
        return(response)
    def delete(self,id):
        '''
            urlBasefun+ms/cms/ad_position/delete.do
        :param id:
        :return:
        '''
        url = modeladverInfo().urlBasefun() +"ms/cms/ad_position/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modeladverInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)

    def AccurateSearch(self, id):
        url = modeladverInfo().urlBasefun() + "ms/cms/ad_position/info/%s.do" % id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % modeladverInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return  response
    def publish(self,id):
        '''
            urlBasefun+ms/cms/ad_position/publish.do
        :param id:
        :return:
        '''
        url = modeladverInfo().urlBasefun() +"ms/cms/ad_position/publish.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modeladverInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)



if __name__ == '__main__':
    baseGo = modeladverInfo()
    modelId=4
    print(baseGo.delete(modelId))






