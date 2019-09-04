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


class leaveMsgUI010(FootlboTestCase):
    '''
        非合作商页面右侧留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT", "Help"


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
        except Exception as e:
            raise IOError
        finally:
            driver.quit()


    def post_test(self):
        # self.driver.quit()
        self.log_info("testOver")


if __name__ == '__main__':
    leaveMsgUI010().debug_run()

