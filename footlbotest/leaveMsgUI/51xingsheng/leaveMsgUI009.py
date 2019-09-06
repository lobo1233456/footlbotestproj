#!user/bin/env python3
# -*- coding: UTF-8 -*-
import random
import time

from retrying import retry
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, ElementClickInterceptedException
from selenium.webdriver.support.select import Select

from footlbolib.testcase import FootlboTestCase



class leaveMsgUI009(FootlboTestCase):
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
            u"(.//*[normalize-space(text()) and normalize-space(.)='《服务条款》'])[1]/following::img[1]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::select[1]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::select[1]")).select_by_visible_text(
            u"河北省")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::option[4]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::select[2]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::select[2]")).select_by_visible_text(
            u"秦皇岛市")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::option[39]").click()
        Select(driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::select[3]")).select_by_visible_text(
            u"101-150㎡")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::option[52]").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::input[1]").send_keys(
            "13764743157")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='装饰建材的猫腻防不胜防,如何才能避免被坑呢!'])[1]/following::p[2]").click()


        time.sleep(2)
        msg = self.close_alert_and_get_its_text(driver)
        self.log_info(msg)
        self.assert_("检查成功提交的结果", u"报价有疑问？装修管家稍后致电为您解答" == msg)



    def post_test(self):
        self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI009().debug_run()

