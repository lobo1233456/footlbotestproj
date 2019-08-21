# -*- coding: utf-8 -*-
'''ʾ����������
'''
#2019/07/31 QTAF�Զ�����

from testbase import testcase

class FootlboTestCase(testcase.TestCase):
    '''foo������������
    '''

    def comparsion(self, message, value):
        """测试断言，如果value的值不为真，则用例失败，输出对应信息

        :param message:断言失败时的提示消息
        :type  message: str
        :param value:用于判断的值
        :type  value: bool或
        """
        if not value:
            self.log_info("nameNew:%s不通过" % self.newName)
            raise (message + "检查点不通过")
        else:
            pass

