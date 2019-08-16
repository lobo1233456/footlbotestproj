#!user/bin/env python3
# -*- coding: UTF-8 -*-


from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.IndependentDecoration.sysModelApi import roleModelInfo
from footlbolib.testcase import FootlboTestCase


class roleManager001(FootlboTestCase):
    '''
    新建菜单--查询菜单已存在，且信息一致,得到该菜单的roleID--修改信息--确认信息已被修改--删除菜单--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = roleModelInfo()

    def run_test(self):
        baseGo = roleModelInfo()
        dirName = baseGo.nameRandom()
        rootName = baseGo.nameRandom()
        buttonName = baseGo.nameRandom()
        dirButtonName = baseGo.nameRandom()
        dirButtonNameUpdate = baseGo.nameRandom()
        baseGo.creatModel(rootName, 1, 0)  # 执行创建根目录菜单
        rootModelID = baseGo.getModelId()

        findNewRes = baseGo.AccurateSearch(rootModelID)
        self.assert_("创建一级菜单栏是否成功", findNewRes["data"]["modelTitle"] == rootName)
        self.log_info("成功创建一级菜单栏名称:%s,modelID:%s" % (rootName, rootModelID))

        baseGo.creatModel(dirName, 1, rootModelID)  # 在根目录下创建二级目录菜单
        dirModelID = baseGo.getModelId()

        findNewRes = baseGo.AccurateSearch(dirModelID)
        self.assert_("创建二级菜单栏名称是否成功", findNewRes["data"]["modelTitle"] == dirName)
        self.log_info("成功创建二级菜单栏名称:%s,modelID:%s" % (dirName, dirModelID))

        baseGo.creatModel(buttonName, 2, rootModelID)  # 执行创建二级目录按钮
        buttonModelID = baseGo.getModelId()

        findNewRes = baseGo.AccurateSearch(buttonModelID)
        self.assert_("创建二级按钮是否成功", findNewRes["data"]["modelTitle"] == buttonName)
        self.log_info("成功创建二级按钮名称:%s,modelID:%s" % (buttonName, buttonModelID))

        baseGo.creatModel(dirButtonName, 2, dirModelID)  # 执行创建二级目录菜单下创建按钮
        dirModelID_twice = baseGo.getModelId()

        findNewRes = baseGo.AccurateSearch(dirModelID_twice)
        self.assert_("创建二级菜单栏按钮是否成功", findNewRes["data"]["modelTitle"] == dirButtonName)
        self.log_info("成功创建二级菜单栏按钮名称:%s,modelID:%s" % (dirButtonName, dirModelID_twice))

        baseGo.update(dirModelID_twice, dirModelID, dirButtonNameUpdate)
        findNewRes = baseGo.AccurateSearch(dirModelID_twice)
        self.assert_("修改程序是否成功", findNewRes["data"]["modelTitle"] == dirButtonNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")

        baseGo.delete(dirModelID_twice)
        resMql = mysqlCon().comMysql("SELECT model_id FROM sys_model where model_id = %s" % dirModelID_twice)
        self.assert_("指定id是否已经被清理", (len(resMql) == 0))
        self.log_info("成功删除指定id的记录")

        self.log_info("清理根目录数据")
        baseGo.delete(rootModelID)


    def post_test(self):
        pass


if __name__ == '__main__':
    roleManager001().debug_run()

