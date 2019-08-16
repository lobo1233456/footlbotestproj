# -*- coding: GBK -*-
'''示
'''
#2019/05/24 QTAF

from footlbolib.testcase import FootlboTestCase
from footlbotest.check import string_combine


class HelloTest(FootlboTestCase):
    '''
    QTA会依照以下顺序执行测试用例的三个接口:
    pre_test
    run_test
    post_test
    且任意一个接口执行异常，QTA仍然会执行下一个接口。
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "Demo","Help"

    def pre_test(self):
        super(HelloTest, self).pre_test()
        self.log_info("hello testcase1")

    def run_test(self):
        # ---------------------------
        self.start_step("测试字符串拼接")
        # ---------------------------
        result = string_combine("xxX",'yy')
        self.assert_("检查string_combine调用结果", result == "xxXyy")
        self.assert_equal(True, True)


    def post_test(self):
        super(HelloTest, self).post_test()
        self.log_info("hello testcase3")


    
if __name__ == '__main__':
    HelloTest().debug_run()

