#!user/bin/env python3
# -*- coding: UTF-8 -*-
import json
import requests
from testbase import datadrive

from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.IndependentDecoration.urlBase import urlInfo
from footlbolib.testcase import FootlboTestCase

@datadrive.DataDrive([
    {"roleID": 2,  "__attrs__": {"priority": FootlboTestCase.EnumPriority.BVT,"tags":"control" }},
    {"roleID": 1,  "__attrs__": {"priority": FootlboTestCase.EnumPriority.High } },
    {"roleID": 4,  "__attrs__": {"priority": FootlboTestCase.EnumPriority.Low } },

])
class sysManager001(FootlboTestCase):
    '''
    新建账号--查询账号已存在，且信息一致,得到该账号的managerID--删除账号--查询账号已删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"
    def pre_test(self):
        self.log_info('新建角色roleID: %s'%self.casedata['roleID'])
        self.url =  urlInfo()
        # ------------获得session---------------
        self.log_info(self.url.keepSession())
    def run_test(self):
        # ---------------------------
        self.start_step("登录验证")
        # ---------------------------
        url = self.url.urlBasefun()+"ms/sys/sys_manager/save.do"
        self.log_info("创建新用户%s"%self.url.nameRandom())
        self.newName =self.url.nameRandom()
        payload = {
              "createBy": 0,
              "createDate": "2019-08-01T01:25:03.800Z",
              "createDateStr": "string",
              "del": 0,
              "managerName": "%s"%self.newName,
              "managerNickname": "strog",
              "managerPassword": "string",
              "managerSalt": "string",
              "roleIdList": [
                self.casedata['roleID']
              ],
              "updateBy": 0,
              "updateDate": "2019-08-01T01:25:03.800Z",
              "updateDateStr": "string"
        }
        self.headers = {
            'Cookie': 'accountName = liubo;%s' % self.url.keepSession()
        }
        responseAdd = requests.request("POST", url, json=payload, headers=self.headers)
        self.log_info("新增接口返回response:%s"%responseAdd)
        nameList = self.mysql.searchMysql()
        self.log_info(r"查找数据库是否存在该账户:"+str(self.newName in nameList))
        if (self.newName in nameList) == True:
            self.log_info("添加成功，数据库中已经含有%s,添加功能已经实现"%self.newName)
        #索引获取manager_id
        urlList  = self.url.urlBasefun()+"ms/sys/sys_manager/list.do"
        querystring = {"sortOrder": "asc", "pageSize": "10", "pageNumber": "1", "pageNo": "1"}
        responseList = requests.request("POST", urlList, headers=self.headers, params=querystring)
        responseList = json.loads(responseList.text)
        self.managerId =  responseList['data']['list'][0]['managerId']
        #获得最新的managerID
        self.log_info("新增账号的managerId：%s"%responseList['data']['list'][0]['managerId'])

    def post_test(self):
        # 删除该账号
        urldel = self.url.urlBasefun() + "ms/sys/sys_manager/delete.do"
        payload = "[%s]"%self.managerId
        response = requests.request("POST", urldel, data=payload, headers=self.headers)
        self.log_info("删除功能response：%s"%response.text)
        #从数据库中验证是否已经删除
        nameList = mysqlCon().searchMysql()
        self.log_info(r"查找数据库是否存在该账户:" + str(self.newName in nameList))
        # print(self.newName,nameList)
        urlCheck = self.url.urlBasefun() + "ms/sys/sys_manager/info/%s.do" % self.managerId
        responseCheck = requests.request("POST", urlCheck, data=payload, headers=self.headers)
        responseCheck = json.loads(responseCheck.text)
        self.log_info("调用查找接口response：%s"%responseCheck)
        if (self.newName in nameList) == False and responseCheck['data'] ==None:
            self.log_info("添加成功，数据库中已经不含有%s,删除功能已经实现" % self.newName)
            self.log_info("新增账号已清理")
        else:raise("账号未被清理")


if __name__ == '__main__':
    sysManager001().debug_run()

