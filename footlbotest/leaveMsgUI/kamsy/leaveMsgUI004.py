#!user/bin/env python3
# -*- coding: UTF-8 -*-
import os
import time

import time

from retrying import retry

from footlbolib.testcase import FootlboTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)

class leaveMsgUI004(FootlboTestCase):
    '''
    底部留言咨询中免费电话
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "Demo", "Help"

    def pre_test(self):
        self.driver = webdriver.Firefox()
        self.accept_next_alert = True

    @retry(stop_max_attempt_number=3, retry_on_exception=retry_if_io_error)
    def run_test(self):
        try:
            driver = self.driver
            driver.get("https://www.kmway.com/")
            driver.maximize_window()
            driver.find_element_by_xpath(u"/html/body/div[5]/div[3]/div/div[4]/table/tbody/tr[68]/td[5]/a").click()
            time.sleep(2)
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='会员服务'])[1]/following::img[3]").click()
            # #页面上的跳转按钮
            # driver.find_element_by_id("freebtn").click()
            # 滚动至元素eles可见位置
            eles = driver.find_element_by_xpath('//*[@id="Free_phone_btn_1"]')
            driver.execute_script("arguments[0].scrollIntoView();", eles)
            time.sleep(2)
            driver.find_element_by_id("Free_phone_text_1").click()
            driver.find_element_by_id("Free_phone_text_1").clear()
            driver.find_element_by_id("Free_phone_text_1").send_keys("13764743158")
            driver.find_element_by_id("Free_phone_btn_1").click()
            msg= self.close_alert_and_get_its_text(driver)
            self.log_info(msg)
            time.sleep(2)
            self.assert_("留言成功",u"呼叫成功,请等候来电"==msg)
        except Exception as e:
            raise IOError
        finally:
            driver.quit()



    def post_test(self):
        self.log_info("testOver")
        time.sleep(2)
        self.driver.quit()


if __name__ == '__main__':
    leaveMsgUI004().debug_run()

