import json
import os
import re
import time
from shutil import copytree
import requests
from pathlib import Path

class cleanFunc():
    def __init__(self):
       cwd = os.getcwd()  # 获取当前目录即dir目录下


    def clean(self,testDatadel):
        '''
            清理测试脚本的无用数据
        :param testDatadel:
        :return:
        '''
        files = os.listdir(os.getcwd())  # 列出目录下的文件
        # for file in files:
        #     if os.path.getsize(file) < minSize * 1000:
        #         os.remove(file)  # 删除文件
        #         print(file + " deleted")
        return
    def judgeSuc(self,dir):
        '''
            判断这次构建是否成功，从构建生成的js报告开始查找,成功包含俩点，用例全部通过和用例执行过程中并未异常
        :param dir: dir的路径
        :return:
        '''
        casePassSuc, allsuc, caseCrashSuc = False, False, False
        with open(r'%s\qta-report.js' % dir, "r") as f:
            data_func = f.read()  # 读取js文件
        caseFail = re.findall(r'"succeed": (true|false), "', data_func)  # 判断用了是否全部通过
        if caseFail[0] == 'true': casePassSuc = True
        enp = re.findall(r'"load_errors": (.*?)"passed_tests"', data_func)  # 取得load_error中的信息
        # 通过js文件中load_error中是否含有字母来判断脚本是否crash,有则错误，没有则正常
        caseCrash = bool(re.search('[a-z]', enp[0]))
        if caseCrash == False: caseCrashSuc = True
        # 俩个判断都为真，则认为脚本正常
        allsuc = casePassSuc and caseCrashSuc
        return allsuc

    def findNewdir(self,dir):
        '''
        在脚本报告目录寻找最新创建的报告
        :param dir:目标目录
        :return:返回该目录下最新创建的文件
        '''
        # a = os.path.getatime(dir)  # 输出最近访问时间
        b = os.path.getctime(dir)  # 输出文件创建时间
        # c = os.path.getmtime(dir)  # 输出最近修改时间
        d = time.gmtime(os.path.getmtime(dir))  # 以struct_time形式输出最近修改时间
        file_lists = os.listdir(dir)  # 输出文件夹下目录
        file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
        if not os.path.isdir(dir + "\\" + fn) else 0)
        p = os.path.join(dir, file_lists[-1])  # 输出最新文件的目录
        return p,file_lists[-1]
    def saveWrongReporter(self,dir,projectDirRoot):
        '''
            保存错误报告到项目中指定位置test_result/test_result_wrong
            同时发送dingding
        :param dir: 所有报告的路径
        :return:返回错误报告
        '''
        enp = self.findNewdir(dir)[0]  # 获得该报告路径
        enpdirName = self.findNewdir(dir)[1]  # 获得该报告名称
        content = '请及时查看错误报告：%s'%enpdirName
        # print(enp, enpdirName)
        # print(self.judgeSuc(enp))
        if self.judgeSuc(enp) == False: #如果报告存在脚本未跑通的情况
            copytree(enp, projectDirRoot + r"\test_result\test_result_wrong\%s" % enpdirName)
            self.dingTalkSend(content)
        else:
            # copytree(enp, r"../../test_result/test_result_wrong/%s" % enpdirName)
            pass
        return enpdirName

    def dingTalkSend(self, content):
        '''
        钉钉固定推送

        targetToken = 0609d4c6c66900d43ea42e1d9e6510825424171cae211c0f648a70662b807460
        :param content: 推送信息
        :return:
        '''
        url = "https://oapi.dingtalk.com/robot/send?access_token=ac2931327c6b5c30f3c9d22e40cf9a05db6c5379170a7c8423205d2eac0ef957"
        headers = {"Content-Type": "application/json ;charset=utf-8 "}
        # content = "测试"
        msg = {
            "msgtype": "text",
            "text": {"content": content}
        }
        post_data = json.dumps(msg)  # 将Python对象编码成 JSON 字符串
        status = requests.post(url, data=post_data, headers=headers)
        msg = {
            "msgtype": "text",
            "text": {"content": content},
            "at": {
                "atMobiles": [
                    "139xxxx0217",
                    "189xxxx8325"],
                "isAtAll": False
            }
        }
        return status.json()
    def historyDel(self,dir):
        '''
            删除指定目录中的，一定时间之后的历史报告
        :param dir:目标目录
        :return:返回该目录下最新创建的文件
        '''
        # a = os.path.getatime(dir)  # 输出最近访问时间
        b = os.path.getctime(dir)  # 输出文件创建时间
        # c = os.path.getmtime(dir)  # 输出最近修改时间
        d = time.gmtime(os.path.getmtime(dir))  # 以struct_time形式输出最近修改时间
        file_lists = os.listdir(dir)  # 输出文件夹下目录
        file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
        if not os.path.isdir(dir + "\\" + fn) else 0)
        p = os.path.join(dir, file_lists[-1])  # 输出最新文件的目录
        return file_lists


if __name__ == '__main__':
    '''
        1,保存错误报告
        2,发送错误信息，通过dingding
        不采用settings的方式引用root目录，是因为cmd模式解决不了这个问题
        
    '''
    fun  = cleanFunc()
    project = r"\footlbotestproj"#项目名称
    proj_root = str(Path.home()) + project
    exlib_dir = proj_root+( r'\test_result\htmlRes')
    print(proj_root,exlib_dir)
    fun.saveWrongReporter(exlib_dir,proj_root)











    # lob = cleanFunc()
    # # projectDirRoot =settings.PROJECT_ROOT_DIR
    # projectDirRoot = r"C:\Users\liubo\footlbotestproj"
    # dir =projectDirRoot + r'\test_result\htmlRes'
    #
    #
    # wrRepor = lob.saveWrongReporter(dir,projectDirRoot) #保存错误报告
    # # #
    # #
    #




