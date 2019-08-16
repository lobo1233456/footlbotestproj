#!user/bin/env python3
# -*- coding: UTF-8 -*-
import json
import time

from retrying import retry
from selenium import webdriver
from footlbolib.testcase import FootlboTestCase
class leaveMsgUI001(FootlboTestCase):
    '''
        非合作商页面右侧留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "Demo", "Help"

    def pre_test(self):
        self.driver = webdriver.Firefox()
        self.accept_next_alert = True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    @retry(stop_max_attempt_number=3, stop_max_delay=10000)
    def run_test(self):
        driver = self.driver
        driver.get("https://www.kmway.com/")
        driver.find_element_by_xpath(u"/html/body/div[5]/div[3]/div/div[4]/table/tbody/tr[68]/td[5]/a").click()
        driver.find_element_by_name("tel").click()
        driver.find_element_by_name("tel").clear()
        driver.find_element_by_name("tel").send_keys("13764743157")
        driver.find_element_by_id("area-right-but1").click()
        time.sleep(2)
        msg = self.close_alert_and_get_its_text()
        self.log_info(msg)
        self.assert_("检查成功提交的结果", u"呼叫成功,请等候来电" == msg)

    def post_test(self):
        self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI001().debug_run()

