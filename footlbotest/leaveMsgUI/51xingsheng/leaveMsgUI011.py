#!user/bin/env python3
# -*- coding: UTF-8 -*-

import time

from retrying import retry
from selenium import webdriver
from selenium.webdriver.support.select import Select
from footlbolib.testcase import FootlboTestCase


class leaveMsgUI011(FootlboTestCase):
    '''
        非合作商页面右侧留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT"


    def retry_if_io_error(exception):
        """Return True if we should retry (in this case when it's an IOError), False otherwise"""
        return isinstance(exception, IOError)

    def pre_test(self):
        self.accept_next_alert = True

    @retry(stop_max_attempt_number=3,retry_on_exception=retry_if_io_error)
    def run_test(self):
        try:
            self.driver = webdriver.Firefox()
            driver = self.driver
            driver.get("https://www.51xinsheng.com/ctbj/")
            driver.find_element_by_link_text(u"0元设计").click()
            driver.find_element_by_id("form_select_one").click()
            Select(driver.find_element_by_id("form_select_one")).select_by_visible_text(u"天津市")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='所在城市：'])[1]/following::option[3]").click()
            driver.find_element_by_id("form_select_two").click()
            Select(driver.find_element_by_id("form_select_two")).select_by_visible_text(u"天津城区")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='所在城市：'])[1]/following::option[37]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='房屋面积：'])[1]/following::select[1]").click()
            Select(driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='房屋面积：'])[1]/following::select[1]")).select_by_visible_text(
                u"61-80㎡")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='房屋面积：'])[1]/following::option[3]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码：'])[1]/following::input[1]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码：'])[1]/following::input[1]").clear()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码：'])[1]/following::input[1]").send_keys(
                "13764743157")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='手机号码：'])[1]/following::div[1]").click()



            time.sleep(2)
            msg = driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/p").text
            # msg = self.close_alert_and_get_its_text(driver)
            self.log_info(msg)
            self.assert_("检查成功提交的结果", u"星装已收到你的需求，我们将安排装修管家与您沟通装修细节，请注意接听电话" == msg)
        except Exception as e:
            raise IOError
        finally:
            driver.quit()


    def post_test(self):
        # self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI011().debug_run()

