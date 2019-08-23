# -*- coding: GBK -*-

import time
import json
import requests
from testbase import resource
from urllib3 import encode_multipart_formdata

import settings
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon

urlBase= settings.URlBASE
class reviewInfo():
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
        url = reviewInfo().urlBasefun() +"ms/cms/review_reviews/save.do"
        payload = {
            "redirect":"","id":"","content":newName,"reviewType":"0"
            }


        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self):
        url = reviewInfo().urlBasefun() +"ms/cms/review_reviews/list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%reviewInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,appId,newName):
        url = reviewInfo().urlBasefun() +"ms/cms/review_reviews/update.do"
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
            'Cookie': "%s"%reviewInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        # response = json.loads(response.text)
        return(response)
    def delete(self,id):
        url = reviewInfo().urlBasefun() +"ms/cms/review_reviews/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%reviewInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)

        return(response.text)

    def AccurateSearch(self, id):
        url = reviewInfo().urlBasefun() + "ms/cms/review_reviews/info/%s.do" % id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % reviewInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return  response

    def upfilisBatch(self,path):
        url = "http://csf.91clt.com:8090/fycms/file/upload.do"
        f1 = open(r'C:\Users\liubo\Desktop\pingLun1234.xlsx','rb')
        files = {
                'file':('pingLun.xlsx',f1,"multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW"),

                 }  # 显式的设置文件名
        data = {
            "name": "pingLun1234.xlsx",
            "maxSize": "200",
            "allowedFile": "xlsx",
            "uploadPath": "reviews"
        }
        headers = {
            # 'content-type': "multipart/form-data", 不能加这个
            'Cookie': "%s" % reviewInfo()._keepSession(),
        }
        response = requests.request("POST", url,data=data,files=files,headers=headers)
        return (response.text)


if __name__ == '__main__':
    baseGo = reviewInfo()
    baseGo.upfilisBatch(r"D:\PycharmProjects\footlbotestproj\resources\FIles\pingLun.xlsx")
    # print(baseGo.GetFiles()
    # for dir_path, dir_names, file_names in test_resources.walk("/"):
    #     log_info("dir_path=%s" % dir_path)
    #

    # siteId=33
    # # print(baseGo.delete("63"))
    # mysqlCon().comMysql("DELETE FROM site_app WHERE app_id = 18")

    # baseGo.update(26,"test123")
    # enp = baseGo.delete(26)
    # res  = re.findall("cn.fy.common.exception.ResultException: (.+)",enp)
    # print(res)
# # import requests
#     name = '60'
#     url = "http://csf.91clt.com:8090/fycms/ms/cms/review_reviews/delete.do"
#     payload = "[\r\n  %s\r\n]"%name
#     headers = {
#         'Content-Type': "application/json",
#         'Cookie': "%s"%reviewInfo()._keepSession(),
#
#         }
#
#     response = requests.request("POST", url, data=payload, headers=headers)
#
#     print(response.text)






