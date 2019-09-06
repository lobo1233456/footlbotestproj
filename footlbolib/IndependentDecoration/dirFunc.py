import os

import settings


class dirFunc():
    def __init__(self):
        directory = "./dir"
        # os.chdir(directory)  # 切换到directory目标目录
        cwd = os.getcwd()  # 获取当前目录即dir目录下

    def deleteBySize(self,minSize):
        """删除小于minSize的文件（单位：K）"""
        files = os.listdir(os.getcwd())  # 列出目录下的文件
        for file in files:
            if os.path.getsize(file) < minSize * 1000:
                os.remove(file)  # 删除文件
                print(file + " deleted")
        return
    def deleteNullFile(self):
        '''删除所有大小为0的文件'''
        files = os.listdir(os.getcwd())
        for file in files:
            if os.path.getsize(file) == 0:  # 获取文件大小
                os.remove(file)
                print(file + " deleted.")
        return
    def deleteTarget(self,Name):
        '''
        删除指定文件
        :param Name: 指定文件name
        :return:
        '''
        files = os.listdir(os.getcwd())  # 列出目录下的文件
        for file in files:
            if file  == Name:
                os.remove(file)  # 删除文件
        msg = Name + " deleted"
        return msg
    def rootProjecct(self):
        '''

        :param projectName: 项目名称
        :return: 项目root目录，末尾带“\”
        '''
        return  settings.PROJECT_ROOT_DIR

if __name__ == '__main__':
    print(dirFunc().rootProjecct())
