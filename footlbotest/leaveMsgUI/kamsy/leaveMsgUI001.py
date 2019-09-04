#!user/bin/env python3
# -*- coding: UTF-8 -*-

import time

from retrying import retry
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

from footlbolib.testcase import FootlboTestCase


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)


class leaveMsgUI001(FootlboTestCase):
    '''
        非合作商页面右侧留言窗口
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BVT"

    def pre_test(self):
        self.driver = webdriver.Firefox()
        self.accept_next_alert = True

    @retry(stop_max_attempt_number=3,retry_on_exception=retry_if_io_error)
    def run_test(self):
        try:
            driver = self.driver
            driver.get("https://www.kmway.com/")
            driver.find_element_by_xpath(u"/html/body/div[5]/div[3]/div/div[4]/table/tbody/tr[68]/td[5]/a").click()
            driver.find_element_by_name("tel").click()
            driver.find_element_by_name("tel").clear()
            driver.find_element_by_name("tel").send_keys("13764743157")
            driver.find_element_by_id("area-right-but1").click()
            time.sleep(2)
            msg = self.close_alert_and_get_its_text(driver)
            self.log_info(msg)
            self.assert_("检查成功提交的结果", u"呼叫成功,请等候来电" == msg)
        except Exception as e:
            raise IOError
        finally:
            driver.quit()

    def post_test(self):
        self.driver.quit()
        self.log_info("testOver")






if __name__ == '__main__':
    leaveMsgUI001().debug_run()

