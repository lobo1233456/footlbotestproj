#!user/bin/env python3
# -*- coding: UTF-8 -*-
import re

import pysnooper
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.IndependentDecoration.siteAppMangerAPi import SiteInfo
from footlbolib.testcase import FootlboTestCase

class SiteManager(FootlboTestCase):
    '''
    新建Site--查询Site已存在，且信息一致,得到该Site的SiteInfoID--修改信息--确认信息已被修改--删除Site--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = SiteInfo()

    @pysnooper.snoop()
    def run_test(self):
        baseGo = SiteInfo()
        siteNew = baseGo.nameRandom()
        siteNameUpdate = baseGo.nameRandom()
        baseGo.creatID(siteNew)
        res  = baseGo.FindID()
        siteId = res["data"]["list"][0]["appId"]
        findNewRes = baseGo.AccurateSearch(siteId)
        self.assert_("创建site是否成功", findNewRes["data"]["appTitle"] == siteNew)
        self.log_info("成功创建site名称:%s,siteId:%s" % (siteNew, siteId))

        baseGo.update(siteId,siteNameUpdate)
        findNewRes = baseGo.AccurateSearch(siteId)
        self.assert_("修改程序是否成功", findNewRes["data"]["appTitle"] == siteNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")


        enp = baseGo.delete(siteId)
        res = re.findall("cn.fy.common.exception.ResultException: (.+)", enp)
        self.assert_("删除功能权限是否开放", res[0] == '该操作危险，系统暂不开放')
        mysqlCon().comMysql("DELETE FROM site_app WHERE app_id = %s" % siteId)
        resMql = mysqlCon().comMysql("SELECT * FROM site_app WHERE app_id = %s" % siteId)
        self.log_info(resMql)
        self.assert_("指定id是否已经被清理", (len(resMql) == 0))

    def post_test(self):
        pass


if __name__ == '__main__':
    SiteManager().debug_run()

