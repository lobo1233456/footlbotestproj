# from testbase.testcase import TestCase
# from testbase.retry import Retry
# def string_combine(a,b):
#     return a+"b"
#
# class StrCombineTest(TestCase):
#     '''测试字符串拼接接口
#     '''
#     owner = "foo"
#     status = TestCase.EnumStatus.Ready
#     priority = TestCase.EnumPriority.Normal
#     timeout = 1
#
#     def run_test(self):
#         for item in Retry(timeout=2, interval=0.5):
#             print(item)
#             # ---------------------------
#             self.start_step("用例断言失败")
#             # ---------------------------
#             self.assert_("断言失败", False)
#
#             # ---------------------------
#             self.start_step("断言失败后置步骤")
#             # ---------------------------
#             self.log_info("hello")
#
#
# if __name__ == '__main__':
#     StrCombineTest().debug_run()
