# -*- coding: GBK -*-
import re
import time
import json
import requests
import settings

urlBase= settings.URlBASE
class pageInfo():
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
        url = pageInfo().urlBasefun() +"ms/custom/page/save.do"
        payload = {
            "redirect": "", "pageId": "", "pageTitle": newName, "pageUrl": "test/%s"%newName, "pagePath": "h5/test.template.html"
        }

        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self):
        url = pageInfo().urlBasefun() +"ms/custom/page/list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%pageInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,appId,newName):
        url = pageInfo().urlBasefun() +"ms/custom/page/update.do"
        payload = {
            "redirect": "", "pageId": appId, "pageTitle": newName, "pageUrl": "test/%s"%newName, "pagePath": "h5/test.template.html"
        }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%pageInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        # response = json.loads(response.text)
        return(response)
    def delete(self,id):
        '''
            http://csf.91clt.com:8090/fycms/ms/custom/page/delete.do
        :param id:
        :return:
        '''
        url = pageInfo().urlBasefun() +"ms/custom/page/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%pageInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)

    def AccurateSearch(self, id):
        url = pageInfo().urlBasefun() + "ms/custom/page/info/%s.do" % id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % pageInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return  response


if __name__ == '__main__':
    baseGo = pageInfo()
    pageId=4
    print(baseGo.delete(pageId))
    # mysqlCon().comMysql("DELETE FROM page_app WHERE app_id = 18")
    # baseGo.update(26,"test123")
    # enp = baseGo.delete(26)
    # res  = re.findall("cn.fy.common.exception.ResultException: (.+)",enp)
    # print(res)
# # import requests
#     name = '60'
#     url = "http://csf.91clt.com:8090/fycms/ms/custom/page/delete.do"
#     payload = "[\r\n  %s\r\n]"%name
#     headers = {
#         'Content-Type': "application/json",
#         'Cookie': "%s"%pageInfo()._keepSession(),
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#     print(response.text)






