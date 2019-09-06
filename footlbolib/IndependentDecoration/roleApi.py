# -*- coding: GBK -*-
import os
import re
import time
import json
import requests
import settings
urlBase= settings.URlBASE
class roleInfo():
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
        url = roleInfo().urlBasefun() +"ms/sys/sys_role/save.do"

        payload = {"roleName":"%s"%newName,"roleId":"","appId":"0","modelIdList":[]}
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self,Name):
        url = roleInfo().urlBasefun() +"ms/sys/sys_role/list.do"

        querystring = {"roleName": "%s"%Name}
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%roleInfo()._keepSession(),
        }
        response = requests.request("POST", url, params=querystring, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,roleId,roleName):
        url = roleInfo().urlBasefun() +"ms/sys/sys_role/update.do"
        payload = {
            "appId": 0,
            "createBy": 0,
            "createDate": "2019-08-13T06:22:31.386Z",
            "createDateStr": "string",
            "del": 0,
            "modelIdList": [
            1
            ],
            "roleId": roleId,
            "roleName": "%s"%roleName,
            "updateBy": 0,
            "updateDate": "2019-08-13T06:22:31.386Z",
            "updateDateStr": "string"
            }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%roleInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response)
    def delete(self,id):
        url = roleInfo().urlBasefun() +"ms/sys/sys_role/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%roleInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        response = json.loads(response.text)
        return(response)
if __name__ == '__main__':
    baseGo = roleInfo()

    print(baseGo.delete("63"))
# # import requests
#     name = '60'
#     url = "http://csf.91clt.com:8090/fycms/ms/sys/sys_role/delete.do"
#
#     payload = "[\r\n  %s\r\n]"%name
#     headers = {
#         'Content-Type': "application/json",
#         'Cookie': "%s"%roleInfo()._keepSession(),
#
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#
#     print(response.text)






