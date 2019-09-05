#!user/bin/env python3
# -*- coding: UTF-8 -*-

import time

from retrying import retry
from selenium import webdriver

from selenium.webdriver.support.select import Select

from footlbolib.testcase import FootlboTestCase




class leaveMsgUI010(FootlboTestCase):
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
        self.driver = webdriver.Firefox()
    def run_test(self):

        driver = self.driver
        driver.get("https://www.51xinsheng.com/ctbj/")
        driver.find_element_by_link_text(u"免费报价").click()
        driver.find_element_by_id("form_select_one").click()
        Select(driver.find_element_by_id("form_select_one")).select_by_visible_text(u"天津市")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='所在城市：'])[1]/following::option[3]").click()
        driver.find_element_by_id("form_select_two").click()
        Select(driver.find_element_by_id("form_select_two")).select_by_visible_text(u"天津城区")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='所在城市：'])[1]/following::option[37]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='房屋面积：'])[1]/following::select[1]")).select_by_visible_text(
            u"81-100㎡")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='房屋面积：'])[1]/following::option[4]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码：'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码：'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码：'])[1]/following::input[1]").send_keys(
            "13764743157")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='返回首页'])[1]/following::i[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='两个月以上'])[1]/following::input[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='两个月以上'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='两个月以上'])[1]/following::input[1]").send_keys(
            "nimss")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='半个月'])[1]/following::li[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='让我们更了解您的需求优先为您服务'])[1]/following::p[4]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='两个月以上'])[1]/following::div[1]").click()



        time.sleep(2)
        msg = driver.find_element_by_xpath("/html/body/div[5]/div/div[1]/p").text
        # msg = self.close_alert_and_get_its_text(driver)
        self.log_info(msg)
        self.assert_("检查成功提交的结果", u"星装已收到你的需求，我们将安排装修管家与您沟通装修细节，请注意接听电话" == msg)



    def post_test(self):
        self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI010().debug_run()

