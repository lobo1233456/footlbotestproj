#!user/bin/env python3
# -*- coding: UTF-8 -*-

import time
from retrying import retry
from selenium import webdriver
from selenium.webdriver.support.select import Select

from footlbolib.testcase import FootlboTestCase



class leaveMsgUI006(FootlboTestCase):
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
        # i = random.randint(7,9)
        # print("----------%s-----------"%i)
        driver.get("https://www.51xinsheng.com/ctbj/")
        driver.find_element_by_link_text(u"装修公司").click()
        time.sleep(2)
        js = "var q=document.documentElement.scrollTop=600"
        driver.execute_script(js)
        time.sleep(3)
        Select(driver.find_element_by_xpath(
            "/html/body/div[5]/div[2]/div[2]/div/div[3]/select[1]")).select_by_visible_text(u"河南省")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::select[1]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::select[1]")).select_by_visible_text(
            u"山西省")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::option[5]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::select[2]")).select_by_visible_text(
            u"阳泉市")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::option[39]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::select[3]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::select[3]")).select_by_visible_text(
            u"81-100㎡")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::option[51]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::input[1]").send_keys(
            "13764743157")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::div[26]").click()

        time.sleep(2)
        msg = self.close_alert_and_get_its_text(driver)
        self.log_info(msg)
        self.assert_("检查成功提交的结果", u"留言待审核" == msg)






    def post_test(self):
        # self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI006().debug_run()

