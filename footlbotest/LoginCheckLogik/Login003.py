#!user/bin/env python3
# -*- coding: UTF-8 -*-
import json

import pysnooper
import requests
from testbase import datadrive
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.IndependentDecoration.urlBase import urlInfo
from footlbolib.testcase import FootlboTestCase
testdata = [
        "111",
        "",
        "11111111111111111111111111111111",
        "$%^ &#",
        " ",
        "{\"a\",1}",
        "-1231233333333333333333333333333333333333",
        "-1",
        r"/n/r/t ,.><?*$&%~",
        r"ஜღ℡♬€✎等"
        "2147483648",
        "-2147483648"
]
@datadrive.DataDrive(testdata)
class Login003(FootlboTestCase):
    '''
    login用户名错误输入，数据驱动模式
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "Demo", "Help"

    def pre_test(self):
        nameList = mysqlCon().searchMysql()
        self.log_info(self.casedata)
        self.assert_("已确定无%s的账号信息:",mysqlCon().existName(nameList,self.casedata))
        self.log_info("已确定无%s的账号信息"%self.casedata)
        self.url =  urlInfo()

    def run_test(self):
        # ---------------------------
        self.start_step("login用户名错误输入：%s"%self.casedata)
        # ---------------------------
        url = self.url.urlBasefun()+"ms/check_login.do"
        payload = {
          "accountName": "%s"%self.casedata,
          "checkCode": "",
          "password": "123456"
        }
        headers = {
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        self.log_info(response.text)
        text = json.loads(response.text)
        self.log_info(text["msg"])
        self.log_info(response.status_code)
        self.assert_("检查login调用结果:", response.status_code ==200)
        self.assert_("提示信息:", text["msg"] == "账号不存在或密码错误")

    def post_test(self):
        self.log_info("testOver")


if __name__ == '__main__':
    Login003().debug_run()

