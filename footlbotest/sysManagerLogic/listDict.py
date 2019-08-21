#!user/bin/env python3
# -*- coding: UTF-8 -*-

import pysnooper

from footlbolib.IndependentDecoration.dictListApi import DictInfo
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.testcase import FootlboTestCase

class dictManager(FootlboTestCase):
    '''
    新建dict--查询dict已存在，且信息一致,得到该dict的dictInfoID--修改信息--确认信息已被修改--删除dict--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = DictInfo()

    @pysnooper.snoop()
    def run_test(self):

        baseGo = DictInfo()
        dictNew = baseGo.nameRandom()
        dictNameUpdate = baseGo.nameRandom()
        baseGo.creatID(dictNew)
        res  = baseGo.FindID()
        dictId = res["data"]["list"][0]["dictId"]
        findNewRes = baseGo.AccurateSearch(dictId)
        self.assert_("创建dict是否成功", findNewRes["data"]["dictName"] == dictNew)
        self.log_info("成功创建dict名称:%s,modelID:%s" % (dictNew, dictId))

        baseGo.update(dictId,dictNameUpdate)
        findNewRes = baseGo.AccurateSearch(dictId)
        self.assert_("修改程序是否成功", findNewRes["data"]["dictName"] == dictNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")

        baseGo.delete(dictId)
        resMql = mysqlCon().comMysql("SELECT * FROM custom_dict WHERE dict_id = %s" % dictId)
        self.assert_("指定id是否已经被清理", (len(resMql) == 0))

    def post_test(self):
        pass


if __name__ == '__main__':
    dictManager().debug_run()

