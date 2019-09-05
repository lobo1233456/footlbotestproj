#!user/bin/env python3
# -*- coding: UTF-8 -*-
import random
import time

from retrying import retry
from selenium import webdriver

from selenium.webdriver.support.select import Select

from footlbolib.testcase import FootlboTestCase


class leaveMsgUI008(FootlboTestCase):
    '''
        非合作商页面右侧留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT"


    def pre_test(self):
        self.accept_next_alert = True

    def run_test(self):

        self.driver = webdriver.Firefox()
        driver = self.driver
        driver.get("https://www.51xinsheng.com/ctbj/")
        driver.find_element_by_link_text(u"装修攻略").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::select[1]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::select[1]")).select_by_visible_text(
            u"天津市")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::option[3]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::select[2]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::select[2]")).select_by_visible_text(
            u"天津城区")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::option[37]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::select[3]")).select_by_visible_text(
            u"81-100㎡")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::option[41]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::input[1]").send_keys(
            "13764743157")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='个名额'])[1]/following::button[1]").click()

        time.sleep(2)
        msg = self.close_alert_and_get_its_text(driver)
        self.log_info(msg)
        self.assert_("检查成功提交的结果", u"报价有疑问？装修管家稍后致电为您解答" == msg)



    def post_test(self):
        # self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI008().debug_run()

