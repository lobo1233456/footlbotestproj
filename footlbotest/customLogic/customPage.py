#!user/bin/env python3
# -*- coding: UTF-8 -*-
import re

import pysnooper

from footlbolib.CustomManage.CustoPageAPI import pageInfo
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

        baseGo = pageInfo()
        pageNew = baseGo.nameRandom()
        pageNameUpdate = baseGo.nameRandom()
        baseGo.creatID(pageNew)
        res  = baseGo.FindID()
        pageId = res["data"]["list"][0]["pageId"]
        findNewRes = baseGo.AccurateSearch(pageId)
        self.assert_("创建page是否成功", findNewRes["data"]["pageTitle"] == pageNew)
        self.log_info("成功创建page名称:%s,modelID:%s" % (pageNew, pageId))

        baseGo.update(pageId,pageNameUpdate)
        findNewRes = baseGo.AccurateSearch(pageId)
        self.assert_("修改程序是否成功", findNewRes["data"]["pageTitle"] == pageNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")

        baseGo.delete(pageId)
        resMql = mysqlCon().comMysql("SELECT * FROM custom_page WHERE page_id = %s" % pageId)
        self.assert_( "指定id是否已经被清理",(len(resMql) == 0))

    def post_test(self):
        pass


if __name__ == '__main__':
    pageManager().debug_run()

