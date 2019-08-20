#!user/bin/env python3
# -*- coding: UTF-8 -*-
import requests
from footlbolib.IndependentDecoration.urlBase import urlInfo
from footlbolib.testcase import FootlboTestCase
class Login001(FootlboTestCase):
    '''
    QTA会依照以下顺序执行测试用例的三个接口:
    pre_test
    run_test
    post_test
    且任意一个接口执行异常，QTA仍然会执行下一个接口。
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT", "Help"

    def pre_test(self):
        self.url =  urlInfo()
    def run_test(self):
        # ---------------------------
        self.start_step("测试登录接口")
        # ---------------------------
        url = self.url.urlBasefun()+"ms/check_login.do"

        payload = {
          "accountName": "liubo",
          "checkCode": "",
          "password": "123456"
        }
        headers = {
        }
        response = requests.request("POST", url, json=payload, headers=headers)
        self.log_info(response.text)
        self.log_info(response.status_code)
        self.assert_("检查login调用结果:", response.status_code ==200)

    def post_test(self):
        self.log_info("void")


if __name__ == '__main__':
    Login001().debug_run()

