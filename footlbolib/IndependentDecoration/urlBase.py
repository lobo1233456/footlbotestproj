# -*- coding: GBK -*-
import re
import time
import requests
import settings

urlBase= settings.URlBASE
class urlInfo(object):
    def __init__(self,accountName='liubo',password='123456'):
        self.accountName  =accountName
        self.password =password

    def urlBasefun(self):
        return urlBase
    def keepSession(self):
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



if __name__ == '__main__':
    pass
    str = urlInfo().keepSession()
    caseFail = re.findall(r'JSESSIONID=(.+?); Path', str)

    print(caseFail[0])

    # PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
    # PROJECT_MODE = "standard"
    # INSTALLED_APPS = []
    # print(PROJECT_ROOT)
