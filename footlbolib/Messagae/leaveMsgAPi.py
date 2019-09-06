# -*- coding: GBK -*-
import re
import time
import json
import requests
import settings

urlBase= settings.URlBASE
class modelMsgInfo():
    def __init__(self,accountName='liubo',password='123456'):
        self.accountName  = accountName
        self.password = password

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
        url = modelMsgInfo().urlBasefun() +"ms/cms/message/save.do"
        payload = {
        "redirect": "",
        "name": "%s"%newName,
        "tel": "13764743167",
        "gender": "0",
        "address": "天府五街地铁站2号b座8楼708",
        "ip": "192.168.6.43",
        "appId": "3",
        "houseType": "2",
        "areaType": "428",
        "decorationTime": "3",
        "message": "test测测测"
    }

        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%self._keepSession()
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindID(self):
        url = modelMsgInfo().urlBasefun() +"ms/cms/message/list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelMsgInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)

    def delete(self,id):
        '''
            urlBasefun+ms/cms/message/delete.do

        :param id:
        :return:
        '''
        url = modelMsgInfo().urlBasefun() +"ms/cms/message/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%modelMsgInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        return(response.text)

    def phone(self,n):
        if re.match(r'1[3,4,5,7,8]\d{9}', n) and len(n)==13:
            print("您输入的的手机号码是：\n", n)
            # 中国联通：
            # 130，131，132，155，156，185，186，145，176
            if re.match(r'13[0,1,2]\d{8}', n) or \
                    re.match(r"15[5,6]\d{8}", n) or \
                    re.match(r"18[5,6]", n) or \
                    re.match(r"145\d{8}", n) or \
                    re.match(r"176\d{8}", n):
                print("该号码属于：中国联通")
            # 中国移动
            # 134, 135 , 136, 137, 138, 139, 147, 150, 151,
            # 152, 157, 158, 159, 178, 182, 183, 184, 187, 188；
            elif re.match(r"13[4,5,6,7,8,9]\d{8}", n) or \
                    re.match(r"147\d{8}|178\d{8}", n) or \
                    re.match(r"15[0,1,2,7,8,9]\d{8}", n) or \
                    re.match(r"18[2,3,4,7,8]\d{8}", n):
                print("该号码属于：中国移动")
            else:
                # 中国电信
                # 133,153,189
                print("该号码属于：中国电信")
        else:
            return ("错误的手机号")




