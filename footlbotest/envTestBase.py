

from testbase.testcase import TestCase

class EnvTestBase(TestCase):

    def pre_test(self):
        super(EnvTestBase, self).post_test()
        print("我在配置环境")
    def post_test(self):
        super(EnvTestBase, self).post_test()

        print("我在清理环境")

class EnvTest4(EnvTestBase):
    '''环境构造测试
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def run_test(self):
        # code 1
        pass

class EnvTest5(EnvTestBase):
    '''环境构造测试
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def run_test(self):
        # code 2
        pass


if __name__ == '__main__':
    EnvTest5().debug_run()
