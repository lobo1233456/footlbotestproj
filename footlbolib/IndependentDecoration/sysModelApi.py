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
        a  = time.time()
        b= round(a,1)
        name  =  "test" + str(b)


        return name
    def creatModel(self,newName,modelType,modelPid):
        '''
        "modelType": 中1指的是菜单，2指的是按钮
        modelPid：父级菜单modelID，菜单只能有俩级，在前端做了限制，后台没有.
                  0指的是根目录
        modelId会随机生成，通过其他接口可以锁定该modelid,
        :param newName: 模块名字
        :param modelType: 模块类型
        :param modelPid: 模块父级id
        :return: 返回该名字
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
            获得数据库model_id最新添加的一个modelID
        :return:最新modelId
        '''
        resMql = mysqlCon().comMysql("SELECT model_id FROM sys_model order by model_id DESC LIMIT 1")
        print(resMql)
        rootModelID = resMql[0][0]
        return  rootModelID

if __name__ == '__main__':
    baseGo = roleModelInfo()
    dirName = baseGo.nameRandom()
    rootName = baseGo.nameRandom()
    buttonName = baseGo.nameRandom()
    dirButtonName = baseGo.nameRandom()
    dirButtonNameUpdate = baseGo.nameRandom()
    baseGo.creatModel(rootName, 1, 0) #执行创建根目录菜单
    rootModelID =baseGo.getModelId()
    print(rootModelID)
    # print("创建一级菜单栏名称:%s,modelID:%s" % (rootName, rootModelID))
    # findNewRes = baseGo.AccurateSearch(rootModelID)
    # assert findNewRes["data"]["modelTitle"] == rootName
    #
    # baseGo.creatModel(dirName, 1, rootModelID)  # 在根目录下创建二级目录菜单
    # dirModelID = baseGo.getModelId()
    # print("创建二级菜单栏名称:%s,modelID:%s" % (dirName, dirModelID))
    # findNewRes = baseGo.AccurateSearch(dirModelID)
    # assert findNewRes["data"]["modelTitle"] == dirName
    #
    # baseGo.creatModel(buttonName, 2, rootModelID)  # 执行创建二级目录按钮
    # buttonModelID = baseGo.getModelId()
    # print("创建二级按钮名称:%s,modelID:%s" % (buttonName, buttonModelID))
    # findNewRes = baseGo.AccurateSearch(buttonModelID)
    # assert findNewRes["data"]["modelTitle"] == buttonName
    #
    # baseGo.creatModel(dirButtonName, 2, dirModelID)  # 执行创建二级目录菜单下创建按钮
    # dirModelID_twice = baseGo.getModelId()
    # print("创建二级菜单栏按钮名称:%s,modelID:%s" % (dirButtonName, dirModelID_twice))
    # findNewRes = baseGo.AccurateSearch(dirModelID_twice)
    # assert findNewRes["data"]["modelTitle"] == dirButtonName
    #
    #
    #
    # print("执行修改程序,修改指定id的Name")
    # baseGo.update(dirModelID_twice,dirModelID,dirButtonNameUpdate)
    # findNewRes = baseGo.AccurateSearch(dirModelID_twice)
    # assert findNewRes["data"]["modelTitle"] == dirButtonNameUpdate #验证是否修改
    # print("删除指定id的记录")
    # baseGo.delete(dirModelID_twice)
    # resMql = mysqlCon().comMysql("SELECT model_id FROM sys_model where model_id = %s"%dirModelID_twice)
    # assert(len(resMql)==0)
    # print("清理根目录数据")
    # baseGo.delete(rootModelID)
    #
    #
    #
    #
    #
    #

