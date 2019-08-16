from testbase.testcase import TestCase
from testbase import datadrive

testdata = [
  "111",
  "",
  "11111111111111111",
  "$%^&#",
]

@datadrive.DataDrive(testdata)
class InvalidUinTest(TestCase):
    '''非法测试号码
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def run_test(self):
        # qq = QQApp()
        # login = LoginPanel(qq)
        #
        # login['uin'] = self.casedata
        # login['passwd'] = "test123"
        # login['login'].click()
        #
        # self.assertEqual(login['tips'].text, "非法帐号")
        print(self.casedata)


if __name__ == '__main__':
    InvalidUinTest().debug_run()