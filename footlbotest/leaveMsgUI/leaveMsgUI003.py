#!user/bin/env python3
# -*- coding: UTF-8 -*-
import json
import time

from footlbolib.testcase import FootlboTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

class leaveMsgUI003(FootlboTestCase):
    '''
        底部标题留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "Demo", "Help"

    def pre_test(self):
        self.driver = webdriver.Firefox()
        self.accept_next_alert = True
    def run_test(self):

        driver = self.driver
        driver.get("https://www.kmway.com/")
        driver.find_element_by_xpath(u"/html/body/div[5]/div[3]/div/div[4]/table/tbody/tr[68]/td[5]/a").click()
        driver.find_element_by_id("bottomTel").click()
        driver.find_element_by_id("bottomTel").clear()
        driver.find_element_by_id("bottomTel").send_keys("13764741358")
        driver.find_element_by_xpath("//div[@id='floatbottom']/div[2]/div/div").click()
        time.sleep(2)
        msg = self.close_alert_and_get_its_text()
        self.log_info(msg)
        time.sleep(2)
        self.assert_equal(u"留言成功", "留言成功！" ==msg)
    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

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
    def post_test(self):
        self.log_info("testOver")
        self.driver.quit()


if __name__ == '__main__':
    leaveMsgUI003().debug_run()

