# -*- coding: GBK -*-
import os
import re
import time
import json
import requests
import settings
from decimal import *

from footlbolib.IndependentDecoration.mysqlCon import mysqlCon

urlBase= settings.URlBASE
class roleModelInfo():
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
    def creatModel(self,newName,modelType,modelPid):
        '''
        "modelType": ��1ָ���ǲ˵���2ָ���ǰ�ť
        modelPid�������˵�modelID���˵�ֻ������������ǰ���������ƣ���̨û��.
                  0ָ���Ǹ�Ŀ¼
        modelId��������ɣ�ͨ�������ӿڿ���������modelid,
        :param newName: ģ������
        :param modelType: ģ������
        :param modelPid: ģ�鸸��id
        :return: ���ظ�����
        '''

        url = roleModelInfo().urlBasefun() +"ms/sys/sys_model/save.do"
        payload ={
            "children": [

            ],
            "hasPerms": 0,
            "modelCode": "",
            "modelIcon": "",
            "modelId": 0,
            "modelPath": "",
            "modelPerms": "cms:message:querytest",
            "modelPid":modelPid,
            "modelSort": 0,
            "modelTitle": "%s"%newName,
            "modelType": modelType,
            "modelUrl": "test/url/"
        }

        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % roleModelInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response,newName)
    def FindModel(self):
        url = roleModelInfo().urlBasefun() +"ms/sys/sys_model/tree_list.do"
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%roleModelInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return(response)
    def update(self,modelId,pid,modelTitle):
        url = roleModelInfo().urlBasefun() +"ms/sys/sys_model/update.do"
        payload = {
          "children": [
          ],
          "hasPerms": 0,
          "modelCode": "",
          "modelIcon": "",
          "modelId": modelId,
          "modelPath": "",
          "modelPerms": "",
          "modelPid": pid,
          "modelSort": 0,
          "modelTitle": "%s"%modelTitle,
          "modelType": 2,
          "modelUrl": "test/url/cecece"
        }

        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%roleModelInfo()._keepSession(),
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        response = json.loads(response.text)
        return(response)
    def delete(self,id):
        url = roleModelInfo().urlBasefun() +"ms/sys/sys_model/delete.do"
        payload = "[\r\n  %s\r\n]"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s"%roleModelInfo()._keepSession(),
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        response = json.loads(response.text)
        return(response)
    def AccurateSearch(self,id):
        url = roleModelInfo().urlBasefun() + "ms/sys/sys_model/info/%s.do"%id
        headers = {
            'Content-Type': "application/json",
            'Cookie': "%s" % roleModelInfo()._keepSession(),
        }
        response = requests.request("POST", url, headers=headers)
        response = json.loads(response.text)
        return (response)
    def getModelId(self):
        '''
            ������ݿ�model_id������ӵ�һ��modelID
        :return:����modelId
        '''
        resMql = mysqlCon().comMysql("SELECT model_id FROM sys_model order by model_id DESC LIMIT 1")
        print(resMql)
        rootModelID = resMql[0][0]
        return  rootModelID


