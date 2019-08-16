# from testbase.plan import TestPlan
# '''
# 文档的意思是执行testcase前，进行清理作用
# '''
# class AndroidAppTestPlan(TestPlan):
#     """Android App test plan
#     """
#     tests = "adtest"
#     test_target_args = "http://package.com/xx.apk"
#
#     def get_test_target(self):
#         """获取被测对象详情
#         """
#         return {"apk": self.test_target_args",
#                 "version": tool_get_apk_ver(self.test_target_args)}
#
#     def test_setup(self, report):
#         """全局初始化
#         """
#         install_tools("adb")
#
#     def resource_setup(self, report, restype, resource):
#         """测试资源初始化
#         """
#         if res_type == "android":
#             adb_install(resource["serialno"], self.test_target_args)
#
# if __name__ == '__main__':
#     AndroidAppTestPlan().debug_run()