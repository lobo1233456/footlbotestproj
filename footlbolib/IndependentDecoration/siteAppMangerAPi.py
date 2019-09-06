# -*- coding: GBK -*-
import re
import time
import json
import requests
import settings
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon

urlBase= settings.URlBASE
class SiteInfo():
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
        url = SiteInfo().urlBasefun() +"ms/sys/site_app/save.do"
        payload = {
                "appCopyright": "dsfs ",
                "appDescription": "3",
                "appId": 0,
                "appKeyword": "1",
                "appLogo": "/upload/0/site_app/5d5611e0e4b00648e33ddf07.png",
                "appMobileTemplate": "pc/test.template.html",
                "appName": "无锡市",
                "appPcTemplate": "string",
                "appPublishTime": "2019-08-16T02:11:36.304Z",
                "appPublishTimeStr": "string",
                "appTitle": "%s"%newName,
                "appUrl": "wxs/%s"%self.nameRandom(),
                "createBy": 0,
                "createDate": "2019-08-16T02:11:36.304Z",
                "createDateStr": "string",
                "del": 0,
                "dictRelationList": [
                    {
                        "dictGroupName": "string",
                        "dictId": 75,
                        "dictName": "string",
                        "foreignId": 0,
                        "groupId": 3,
                        "relationId": 0,
                        "typeId": 0
                    }
                ],
                "remark": "string",
                "updateBy": 0,
                "updateDate": "2019-08-16T02:11:36.304Z",
                "updateDateStr": "string"
            }


        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self):
        url = SiteInfo().urlBasefun() +"ms/sys/site_app/list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%SiteInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,appId,newName):
        url = SiteInfo().urlBasefun() +"ms/sys/site_app/update.do"
        payload = {
                "appCopyright": "dsfs ",
                "appDescription": "3",
                "appId": appId,
                "appKeyword": "1",
                "appLogo": "/upload/0/site_app/5d5611e0e4b00648e33ddf07.png",
                "appMobileTemplate": "pc/test.template.html",
                "appName": "无锡市",
                "appPcTemplate": "string",
                "appPublishTime": "2019-08-16T02:11:36.304Z",
                "appPublishTimeStr": "string",
                "appTitle": "%s"%newName,
                "appUrl": "wxs/%s"%newName,
                "createBy": 0,
                "createDate": "2019-08-16T02:11:36.304Z",
                "createDateStr": "string",
                "del": 0,
                "dictRelationList": [
                    {
                        "dictGroupName": "string",
                        "dictId": 75,
                        "dictName": "string",
                        "foreignId": 0,
                        "groupId": 3,
                        "relationId": 0,
                        "typeId": 0
                    }
                ],
                "remark": "string",
                "updateBy": 0,
                "updateDate": "2019-08-16T02:11:36.304Z",
                "updateDateStr": "string"
            }
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%SiteInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        # response = json.loads(response.text)
        return(response)
    def delete(self,id):
        url = SiteInfo().urlBasefun() +"ms/sys/site_app/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%SiteInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)

        return(response.text)

    def AccurateSearch(self, id):
        url = SiteInfo().urlBasefun() + "ms/sys/site_app/info/%s.do" % id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % SiteInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return  response


if __name__ == '__main__':
    baseGo = SiteInfo()
    siteId=33
    # print(baseGo.delete("63"))
    mysqlCon().comMysql("DELETE FROM site_app WHERE app_id = 18")

    # baseGo.update(26,"test123")
    # enp = baseGo.delete(26)
    # res  = re.findall("cn.fy.common.exception.ResultException: (.+)",enp)
    # print(res)
# # import requests
#     name = '60'
#     url = "http://csf.91clt.com:8090/fycms/ms/sys/site_app/delete.do"
#     payload = "[\r\n  %s\r\n]"%name
#     headers = {
#         'Content-Type': "application/json",
#         'Cookie': "%s"%SiteInfo()._keepSession(),
#
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#
#     print(response.text)






