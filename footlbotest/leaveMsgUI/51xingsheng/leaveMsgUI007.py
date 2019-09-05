#!user/bin/env python3
# -*- coding: UTF-8 -*-

import time

from retrying import retry
from selenium import webdriver


from footlbolib.testcase import FootlboTestCase




class leaveMsgUI007(FootlboTestCase):
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
        driver.find_element_by_link_text(u"装修公司").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='下一页'])[1]/following::img[3]").click()
        time.sleep(2)
        # driver.find_element_by_xpath(
        #     u"(/html/body/div[6]/div[1]/div[2]/div[5]/div").click()
        driver.find_element_by_xpath(
            u"/html/body/div[6]/div[1]/div[2]/div[5]/div").click()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='免费预约装企上门服务'])[1]/following::input[1]").clear()
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='免费预约装企上门服务'])[1]/following::input[1]").send_keys(
            "13764743157")
        driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='免费预约装企上门服务'])[1]/following::button[1]").click()
        time.sleep(2)
        msg = self.close_alert_and_get_its_text(driver)
        self.log_info(msg)
        self.assert_("检查成功提交的结果", u"预约成功，请注意接听装修管家来电" == msg)


    def post_test(self):
        # self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI007().debug_run()

