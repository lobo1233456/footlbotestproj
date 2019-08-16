# -*- coding: GBK -*-
'''ʾ
'''
#2019/05/24 QTAF

from footlbolib.testcase import FootlboTestCase
from footlbotest.check import string_combine


class HelloTest(FootlboTestCase):
    '''
    QTA����������˳��ִ�в��������������ӿ�:
    pre_test
    run_test
    post_test
    ������һ���ӿ�ִ���쳣��QTA��Ȼ��ִ����һ���ӿڡ�
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
        self.start_step("�����ַ���ƴ��")
        # ---------------------------
        result = string_combine("xxX",'yy')
        self.assert_("���string_combine���ý��", result == "xxXyy")
        self.assert_equal(True, True)


    def post_test(self):
        super(HelloTest, self).post_test()
        self.log_info("hello testcase3")


    
if __name__ == '__main__':
    HelloTest().debug_run()

