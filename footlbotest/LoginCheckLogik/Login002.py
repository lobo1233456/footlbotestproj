#!user/bin/env python3
# -*- coding: UTF-8 -*-
import json
import requests
from testbase import datadrive
from footlbolib.IndependentDecoration.urlBase import urlInfo
from footlbolib.testcase import FootlboTestCase
testdata = [
  "111",
  "",
  "11111111111111111",
  "   $%^& #",
  " ",

]
@datadrive.DataDrive(testdata)
class Login002(FootlboTestCase):
    '''
    login密码错误输入，数据驱动模式
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "Demo", "Help"

    def pre_test(self):
        self.url =  urlInfo()

    def run_test(self):
        # ---------------------------
        self.start_step("login密码错误")
        # ---------------------------
        url = self.url.urlBasefun()+"ms/check_login.do"

        payload = {
          "accountName": "liubo",
          "checkCode": "",
          "password": "%s"%self.casedata
        }
        self.log_info(payload)
        headers = {
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        text = json.loads(response.text)
        self.assert_("检查login调用结果:", response.status_code ==200)
        self.assert_("提示信息:", text["msg"] == "账号不存在或密码错误")

    def post_test(self):
        self.log_info("testOver")


if __name__ == '__main__':
    Login002().debug_run()

