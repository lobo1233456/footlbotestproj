#!user/bin/env python3
# -*- coding: UTF-8 -*-
import re

import pysnooper

from footlbolib.CustomManage.CustoModelFieldAPI import modelFieldInfo
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon

from footlbolib.testcase import FootlboTestCase

class ModelFieldManager(FootlboTestCase):
    '''
    新建ModelField--查询ModelField已存在，且信息一致,得到该ModelField的ModelFieldInfoID--修改信息--确认信息已被修改--删除ModelField--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = modelFieldInfo()

    @pysnooper.snoop()
    def run_test(self):

        baseGo = modelFieldInfo()
        ModelFieldNew = baseGo.nameRandom()
        ModelFieldNameUpdate = baseGo.nameRandom()
        baseGo.creatID(ModelFieldNew)

        resMql = mysqlCon().comMysql("SELECT field_id FROM custom_content_model_field ORDER BY field_id desc LIMIT 1")

        ModelFieldId = resMql[0][0]
        findNewRes = baseGo.FindID(ModelFieldId)
        self.assert_("创建ModelField是否成功", findNewRes["data"]["fieldName"] == ModelFieldNew)
        self.log_info("成功创建ModelField名称:%s,ModelFieldID:%s" % (ModelFieldNew, ModelFieldId))

        baseGo.update(ModelFieldId,ModelFieldNameUpdate)
        findNewRes = baseGo.AccurateSearch(ModelFieldId)
        self.assert_("修改程序是否成功", findNewRes["data"]["fieldName"] == ModelFieldNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")

        baseGo.delete(ModelFieldId)
        mysqlCon().comMysql("DELETE FROM custom_content_model_field WHERE field_id = %s" % ModelFieldId)
        resMql = mysqlCon().comMysql("SELECT * FROM custom_content_model_field WHERE field_id = %s" % ModelFieldId)
        self.assert_( "指定id是否已经被清理",(len(resMql) == 0))


    def post_test(self):
        pass


if __name__ == '__main__':
    ModelFieldManager().debug_run()

