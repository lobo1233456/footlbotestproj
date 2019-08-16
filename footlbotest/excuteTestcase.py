from testbase.testcase import TestCase, RepeatTestCaseRunner

from testbase.testcase import debug_run_all
class RepeatTest(TestCase):
    '''测试示例
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    timeout = 1
    priority = TestCase.EnumPriority.Normal
    case_runner = RepeatTestCaseRunner()
    repeat = 2

    def run_test(self):
        self.log_info('第%s次测试执行' % self.iteration)
class TestA(TestCase):
    '''测试示例
    '''
    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal

    def run_test(self):
        assert False
        pass

class TestB(TestCase):
    '''测试示例
    '''
    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    case_runner = RepeatTestCaseRunner()
    repeat = 2

    def run_test(self):
        pass

class TestC(TestCase):
    '''测试示例
    '''
    timeout = 1
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal

    def run_test(self):
        pass

__qtaf_seq_tests__ = [TestA, TestC,TestB]

if __name__ == '__main__':
    # RepeatTest().debug_run()
    debug_run_all()
