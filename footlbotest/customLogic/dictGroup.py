#!user/bin/env python3
# -*- coding: UTF-8 -*-

import pysnooper
from footlbolib.CustomManage.CustoPageAPI import pageInfo
from footlbolib.CustomManage.dictGroupAPI import dictGroup
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon

from footlbolib.testcase import FootlboTestCase

class pageManager(FootlboTestCase):
    '''
    新建page--查询page已存在，且信息一致,得到该page的pageInfoID--修改信息--确认信息已被修改--删除page--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = pageInfo()

    @pysnooper.snoop()
    def run_test(self):

        baseGo = dictGroup()
        pageNew = baseGo.nameRandom()
        pageNameUpdate = baseGo.nameRandom()
        baseGo.creatID(pageNew)
        res  = baseGo.FindID()
        self.log_info(res)
        pageId = res["data"]["list"][-1]["groupId"]
        findNewRes = baseGo.AccurateSearch(pageId)
        self.assert_("创建page是否成功", findNewRes["data"]["groupCode"] == pageNew)
        self.log_info("成功创建page名称:%s,modelID:%s" % (pageNew, pageId))

        baseGo.update(pageId,pageNameUpdate)
        findNewRes = baseGo.AccurateSearch(pageId)
        self.assert_("修改程序是否成功", findNewRes["data"]["groupCode"] == pageNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")

        baseGo.delete(pageId)
        mysqlCon().comMysql("DELETE FROM custom_dict_group WHERE group_id = %s" % pageId)
        resMql = mysqlCon().comMysql("SELECT * FROM custom_dict_group WHERE group_id = %s" % pageId)
        print(resMql)
        self.assert_( "指定id是否已经被清理",(len(resMql) == 0))

    def post_test(self):
        pass


if __name__ == '__main__':
    pageManager().debug_run()

