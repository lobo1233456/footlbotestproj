import os

from testbase.testcase import TestCase

class HelloTest(TestCase):
    '''文件资源测试用例
    '''
    owner = "foo"
    status = TestCase.EnumStatus.Ready
    priority = TestCase.EnumPriority.Normal
    timeout = 1

    def run_test(self):
        #---------------------------
        self.start_step("测试文件资源管理接口")
        #---------------------------
        for dir_path, dir_names, file_names in self.test_resources.walk(""):
            self.log_info("dir_path=%s" % dir_path)
            self.log_info("dir_names=%s" % dir_names)
            self.log_info("file_names=%s" % file_names)

        items = self.test_resources.list_dir("video")
        for item in items:
            item_file = self.test_resources.get_file(os.path.join("video", item))
            self.log_info(item_file)

        mp4_filepath = self.test_resources.get_file("video/foo.mp4")
        self.assert_equal("文件存在", os.path.isfile(mp4_filepath), True)

        bigfile_path = self.test_resource.get_file("video/bigfile.mp4.link")
        self.assert_equal("文件存在", os.path.isfile(bigfile_path), True)
if __name__ == '__main__':
    HelloTest().debug_run()
