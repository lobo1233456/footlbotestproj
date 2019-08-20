#!user/bin/env python3
# -*- coding: UTF-8 -*-
import json


import requests
from footlbolib.IndependentDecoration.urlBase import urlInfo
from footlbolib.testcase import FootlboTestCase
class Login004(FootlboTestCase):
    '''
    登录--查看登录状态--退出登录--查看登录状态
    检查点,判读前后的功能状态是否一致
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT"

    def pre_test(self):
        self.url =  urlInfo(accountName='admin', password='123456')


    def run_test(self):
        # ---------------------------
        self.start_step("测试登录接口")
        # ---------------------------
        url = self.url.urlBasefun()+"ms/check_login.do"
        payload = {
          "accountName": "admin",
          "checkCode": "",
          "password": "123456"
        }
        response = requests.request("POST", url, json=payload)#执行登录
        self.log_info("执行登录%s"%response.text)
        self.assert_("检查login调用结果:", response.status_code ==200)
        self.headers = {'Cookie': "%s" % response.headers['Set-Cookie']}
        urlCheckStatus = self.url.urlBasefun()+'ms/online_status.do'
        responseStatus = requests.request("GET", urlCheckStatus, headers=self.headers) #执行登录操作状态检查
        self.log_info("登入功能状态%s"%responseStatus.text)
        responseStatusBF = json.loads(responseStatus.text)
        urlLogout =self.url.urlBasefun()+"ms/logout.do"
        requests.request("GET", urlLogout, headers=self.headers) #执行退出操作
        responseStatusAF = requests.request("GET", urlCheckStatus, headers=self.headers) #执行登出操作状态检查
        self.log_info("登出功能状态%s"%responseStatusAF.text)
        responseStatusAF = json.loads(responseStatusAF.text)
        if responseStatusAF['data'] != responseStatusBF['data']:self.log_info("退出登录和登录接口正常")
        else:raise ("退出登录和登录接口不正常")


    def post_test(self):
        self.log_info("testOver")


if __name__ == '__main__':
    Login004().debug_run()

