# -*- coding: GBK -*-

import time
import json
import requests
import settings
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon

urlBase= settings.URlBASE
class DictInfo():
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
        return "test"+str(int(time.time()))
    def creatID(self,newName):
        '''
           Id会随机生成
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
            可以通过dictName索引，参数形式params
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


if __name__ == '__main__':
    baseGo = DictInfo()
    DictId=33
    # print(baseGo.delete("63"))
    mysqlCon().comMysql("DELETE FROM Dict_app WHERE app_id = 18")

    # baseGo.update(26,"test123")
    # enp = baseGo.delete(26)
    # res  = re.findall("cn.fy.common.exception.ResultException: (.+)",enp)
    # print(res)
# # import requests
#     name = '60'
#     url = "http://csf.91clt.com:8090/fycms/ms/custom/dict/delete.do"
#     payload = "[\r\n  %s\r\n]"%name
#     headers = {
#         'Content-Type': "application/json",
#         'Cookie': "%s"%DictInfo()._keepSession(),
#
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#
#     print(response.text)






