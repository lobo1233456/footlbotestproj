#!user/bin/env python3
# -*- coding: UTF-8 -*-

import time
from retrying import retry
from footlbolib.testcase import FootlboTestCase
from selenium import webdriver




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


    def run_test(self):
        #循环次数3次，有一次成功即为通过。
        #通过即停止

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


    def post_test(self):
        self.log_info("testOver")
        self.driver.quit()


if __name__ == '__main__':
    leaveMsgUI003().debug_run()

