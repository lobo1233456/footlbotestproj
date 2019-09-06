#!user/bin/env python3
# -*- coding: UTF-8 -*-
import random
import time

from retrying import retry
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, ElementClickInterceptedException
from selenium.webdriver.support.select import Select

from footlbolib.testcase import FootlboTestCase




class leaveMsgUI003(FootlboTestCase):
    '''
        留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT"




    def pre_test(self):
        self.accept_next_alert = True

    def run_test(self):

        self.driver = webdriver.Chrome()
        driver = self.driver
        driver.maximize_window()

        driver.get("https://www.51xinsheng.com/ctbj/")
        driver.find_element_by_link_text(u"装修公司").click()

        time.sleep(2)
        driver.find_element_by_xpath(
            u"/html/body/div[5]/div[1]/div[2]/div[1]/span").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='免费预约装企上门服务'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='免费预约装企上门服务'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='免费预约装企上门服务'])[1]/following::input[1]").send_keys(
            "13764743157")
        time.sleep(2)
        driver.find_element_by_id(u"commitOrder").click()
        time.sleep(2)
        msg = self.close_alert_and_get_its_text(driver)
        self.log_info(msg)
        self.assert_("检查成功提交的结果", u"预约成功，请注意接听装修管家来电" == msg)

    def post_test(self):
        self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI003().debug_run()

