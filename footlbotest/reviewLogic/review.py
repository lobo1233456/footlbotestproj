#!user/bin/env python3
# -*- coding: UTF-8 -*-
import re

import pysnooper


from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.Review.review_reviews_api import reviewInfo

from footlbolib.testcase import FootlboTestCase

class reviewCase(FootlboTestCase):
    '''
    新建model--查询model已存在，且信息一致,得到该model的reviewInfoID--修改信息--确认信息已被修改--删除model--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = reviewInfo()

    @pysnooper.snoop()
    def run_test(self):

        baseGo = reviewInfo()
        modelNew = baseGo.nameRandom()
        modelNameUpdate = baseGo.nameRandom()
        baseGo.creatID(modelNew)
        res  = baseGo.FindID()
        id = res["data"]["list"][0]["id"]
        findNewRes = baseGo.AccurateSearch(id)
        self.assert_("创建model是否成功", findNewRes["data"]["content"] == modelNew)
        self.log_info(findNewRes["data"]["content"] )
        self.log_info("成功创建model名称:%s,id:%s" % (modelNew, id))

        baseGo.update(id,modelNameUpdate)
        findNewRes = baseGo.AccurateSearch(id)
        self.assert_("修改程序是否成功", findNewRes["data"]["content"] == modelNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")

        baseGo.delete(id)
        # mysqlCon().comMysql("DELETE FROM custom_content_model WHERE model_id = %s" % id)
        resMql = mysqlCon().comMysql("SELECT * FROM custom_content_model WHERE model_id = %s" % id)
        self.assert_( "指定id是否已经被清理",(len(resMql) == 0))


    def post_test(self):
        pass


if __name__ == '__main__':
    reviewCase().debug_run()

