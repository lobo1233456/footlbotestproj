# -*- coding: utf-8 -*-
'''

'''
#2019/07/31 QTAF
from selenium.common.exceptions import NoAlertPresentException
from testbase import testcase

class FootlboTestCase(testcase.TestCase):
    '''
        FootlboTest项目中所有小case们的云爸爸
    '''


    def comparsion(self, message, value):
        """测试断言，如果value的值不为真，则用例失败，输出对应信息
        :param message:断言失败时的提示消息
        :type  message: str
        :param value:用于判断的值
        :type  value: bool或
        """
        if not value:
            self.log_info("nameNew:%s不通过" % self.newName)
            raise (message + "检查点不通过")
        else:
            pass

    def close_alert_and_get_its_text(self,driver):
        try:
            alert = driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def is_alert_present(self,driver):
        try:
            driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

