import os, datetime
import sys
class delFun():
    def delDir(self,dirToBeEmptied,days):
        '''
        删除指定目录下的文件，不是文件夹
        定期处理
        :param dirToBeEmptied: 指定目录
        :param days: now - delta，今日之前的几天
        :return:
        '''
        ds = list(os.walk(dirToBeEmptied))  # 获得所有文件夹的信息列表
        delta = datetime.timedelta(days)  # 设定365天前的文件为过期
        now = datetime.datetime.now()  # 获取当前时间
        for d in ds:  # 遍历该列表
            os.chdir(d[0])  # 进入本级路径，防止找不到文件而报错
            if d[2] != []:  # 如果该路径下有文件
                for x in d[2]:  # 遍历这些文件
                    ctime = datetime.datetime.fromtimestamp(os.path.getctime(x))  # 获取文件创建时间
                    if ctime < (now - delta):  # 若创建于delta天前
                        os.remove(x)  # 则删掉

    def delete_gap_dir(self,dir):
        '''
            清理空文件夹
        :param dir: 指定目录
        :return:
        '''
        for (root, dirs, files) in os.walk(dir):
            for item in dirs:
                dir = os.path.join(root, item)
                try:
                    os.rmdir(dir)  # os.rmdir() 方法用于删除指定路径的目录。仅当这文件夹是空的才可以, 否则, 抛出OSError。
                    print(dir,'已经删除')
                except Exception as e:
                    # print('Exception', e)
                    pass


if __name__ == '__main__':
    #获取项目root目录
    # rootPath = settings.PROJECT_ROOT_DIR
    # rootPath = r"C:\Users\liubo\footlbotestproj"
    #删除7天之前的所有文件数据
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 到suite 目录
    root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
    sys.path.append(root_path)
    rootPath = root_path
    print(rootPath)
    delFun().delDir(rootPath +r'\test_result\htmlRes',1)
    #删除空文件
    delFun().delete_gap_dir(rootPath+r'\test_result\htmlRes')

