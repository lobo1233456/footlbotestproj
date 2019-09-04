#!user/bin/env python3
# -*- coding: UTF-8 -*-

import time

from retrying import retry

from footlbolib.testcase import FootlboTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)


class leaveMsgUI003(FootlboTestCase):
    '''
        底部标题留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT"

    def pre_test(self):
        self.driver = webdriver.Firefox()
        self.accept_next_alert = True

    @retry(stop_max_attempt_number=3, retry_on_exception=retry_if_io_error)
    def run_test(self):
        #循环次数3次，有一次成功即为通过。
        #通过即停止
        try:
            driver = webdriver.Firefox()
            driver.get("https://www.kmway.com/")
            driver.find_element_by_xpath(
                u"/html/body/div[5]/div[3]/div/div[4]/table/tbody/tr[68]/td[5]/a").click()
            driver.find_element_by_id("bottomTel").click()
            driver.find_element_by_id("bottomTel").clear()
            driver.find_element_by_id("bottomTel").send_keys("13764741358")
            driver.find_element_by_xpath("//div[@id='floatbottom']/div[2]/div/div").click()
            time.sleep(2)
            msg = self.close_alert_and_get_its_text(driver)
            self.log_info(msg)
            time.sleep(2)
            self.assert_equal(u"留言成功", "留言成功！" == msg)
        except Exception as e:
            raise IOError
        finally:
                driver.quit()

    def post_test(self):
        self.log_info("testOver")
        self.driver.quit()


if __name__ == '__main__':
    leaveMsgUI003().debug_run()

