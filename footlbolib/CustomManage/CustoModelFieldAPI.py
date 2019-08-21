# -*- coding: GBK -*-
import time
import json
import requests
import settings

urlBase= settings.URlBASE
class modelFieldInfo():
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
            appId会随机生成
        :param newName:
        :return:
        '''
        url = modelFieldInfo().urlBasefun() +"ms/custom/content_model_field/save.do"
        payload = {
            "redirect": "",
            "fieldCmId": "1",
            "fieldId": "",
            "fieldShowName": "tset312",
            "fieldName": "%s"%newName,
            "fieldPluginType": "2",
            "fieldType": "1",
            "fieldNullable": "0",
            "fieldSort": "",
            "fieldThirdSource": "213",
            "fieldDefaultValue": "123",
            "fieldDescription": "33"
        }



        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self,id):
        url = modelFieldInfo().urlBasefun() +"ms/custom/content_model_field/info/%s.do"%id


        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelFieldInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,modelId,newName):
        url = modelFieldInfo().urlBasefun() +"ms/custom/content_model_field/update.do"
        payload = {
            "redirect": "", "modelId": modelId, "modelCode": "1", "modelName": "%s"%newName, "modelDescription": "3"
        }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelFieldInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        # response = json.loads(response.text)
        return(response)
    def delete(self,id):
        '''
            http://csf.91clt.com:8090/fycms/ms/custom/content_model_field/delete.do
        :param id:
        :return:
        '''
        url = modelFieldInfo().urlBasefun() +"ms/custom/content_model_field/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelFieldInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)

    def AccurateSearch(self, id):
        url = modelFieldInfo().urlBasefun() + "ms/custom/content_model_field/info/%s.do" % id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % modelFieldInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return  response


if __name__ == '__main__':
    baseGo = modelFieldInfo()
    modelId=4
    # print(baseGo.FindID(modelId))
    baseGo.delete(modelId)
    # mysqlCon().comMysql("DELETE FROM model_app WHERE app_id = 18")
    # baseGo.update(26,"test123")
    # enp = baseGo.delete(26)
    # res  = re.findall("cn.fy.common.exception.ResultException: (.+)",enp)
    # print(res)
# # import requests
#     name = '60'
#     url = "http://csf.91clt.com:8090/fycms/ms/custom/content_model_field/delete.do"
#     payload = "[\r\n  %s\r\n]"%name
#     headers = {
#         'Content-Type': "application/json",
#         'Cookie': "%s"%modelFieldInfo()._keepSession(),
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#     print(response.text)






