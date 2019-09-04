#!user/bin/env python3
# -*- coding: UTF-8 -*-
import json
import time

from retrying import retry

from footlbolib.testcase import FootlboTestCase
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def retry_if_io_error(exception):
    """Return True if we should retry (in this case when it's an IOError), False otherwise"""
    return isinstance(exception, IOError)


class leaveMsgUI002(FootlboTestCase):
    '''
    底部留言咨询中提交留言
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
        try:
            driver = self.driver
            driver.get("https://www.kmway.com/")
            driver.find_element_by_xpath(u"/html/body/div[5]/div[3]/div/div[4]/table/tbody/tr[68]/td[5]/a").click()
            driver.find_element_by_id("freebtn").click()
            # self.driver.implicitly_wait(30)
            time.sleep(5)
            driver.find_element_by_id("Name1").clear()
            driver.find_element_by_id("Name1").send_keys("test")
            time.sleep(2)
            driver.find_element_by_id("Tel1").click()
            driver.find_element_by_id("Tel1").clear()
            driver.find_element_by_id("Tel1").send_keys("13764743157")
            driver.find_element_by_id("InvestMoney1").click()
            Select(driver.find_element_by_id("InvestMoney1")).select_by_visible_text(u"10-20万")
            driver.find_element_by_id("Email").click()
            driver.find_element_by_id("Email").clear()
            driver.find_element_by_id("Email").send_keys("1009848820@qq.com")
            driver.find_element_by_id("msgProvince1").click()
            Select(driver.find_element_by_id("msgProvince1")).select_by_visible_text(u"河北省")
            driver.find_element_by_id("msgCity1").click()
            Select(driver.find_element_by_id("msgCity1")).select_by_visible_text(u"保定市")
            Select(driver.find_element_by_id("msgXian1")).select_by_visible_text(u"清苑县")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='合作地区'])[1]/following::option[51]").click()
            driver.find_element_by_id("Message").click()
            driver.find_element_by_id("Message").clear()
            driver.find_element_by_id("Message").send_keys(u"cecece测试测试")
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='快捷留言'])[1]/following::p[4]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='快捷留言'])[1]/following::p[3]").click()
            driver.find_element_by_xpath(
                u"(.//*[normalize-space(text()) and normalize-space(.)='快捷留言'])[1]/following::p[2]").click()
            driver.find_element_by_id("yixiang").click()
            driver.find_element_by_id("imgBtnUp1").click()

        # try:
        #     picture_url = driver.get_screenshot_as_file('PicleaveMsgUI002.png')
        #     self.log_info("%s：截图" % picture_url)
        # except BaseException as msgPic:
        #     print(msgPic)
            self.driver.implicitly_wait(30)
            msg = self.close_alert_and_get_its_text(driver)
            self.test_result.info("这个是一个截图", attachments={"留言成功截图": "PicleaveMsgUI002.png"})
            self.log_info(msg)
            self.assert_("检查成功提交的结果", u"留言成功" in msg)

        except Exception as e:
            raise IOError
        finally:
            driver.quit()

    def post_test(self):
        self.log_info("testOver")
        # self.dele.deleteTarget("PicleaveMsgUI002.png")
        self.driver.quit()



if __name__ == '__main__':
    leaveMsgUI002().debug_run()

