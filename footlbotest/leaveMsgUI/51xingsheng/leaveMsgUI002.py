#!user/bin/env python3
# -*- coding: UTF-8 -*-
import random
import time

from retrying import retry
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, NoAlertPresentException, ElementClickInterceptedException
from selenium.webdriver.support.select import Select

from footlbolib.testcase import FootlboTestCase


def w_test(func):
    def inner(*args, **kwargs):
        for i in range(3):
            try:
                func(*args, **kwargs)
                break
            except NoSuchElementException as e:
                pass
            finally:
                i = i + 1
                # driver.quit()
        # return ret
    return inner


class leaveMsgUI002(FootlboTestCase):
    '''
        非合作商页面右侧留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "Demo", "Help"


    def retry_if_io_error(exception):
        """Return True if we should retry (in this case when it's an IOError), False otherwise"""
        return isinstance(exception, IOError)

    def pre_test(self):
        self.accept_next_alert = True
    @retry(stop_max_attempt_number=3,retry_on_exception=retry_if_io_error)
    def run_test(self):

        try:
            self.driver = webdriver.Firefox()
            # i = random.randint(7,9)
            # print("----------%s-----------"%i)
            driver = self.driver
            driver.get("https://www.51xinsheng.com/ctbj/")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::select[1]").click()
            Select(driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::select[1]")).select_by_visible_text(
                u"山东省")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::select[2]").click()
            Select(driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::select[2]")).select_by_visible_text(
                u"聊城市")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::option[51]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::input[1]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::input[1]").clear()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::input[1]").send_keys(
                "13764743157")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::select[3]").click()
            Select(driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::select[3]")).select_by_visible_text(
                u"81-100㎡")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='日式80平二居室装修效果图'])[1]/following::div[9]").click()

            time.sleep(2)
            msg = self.close_alert_and_get_its_text(driver)
            self.log_info(msg)
            self.assert_("检查成功提交的结果", u"预约成功，请注意接听装修管家来电" == msg)
        except Exception as e:
            raise IOError
        finally:
            driver.quit()






    def post_test(self):
        # self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI002().debug_run()

