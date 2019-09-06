#!user/bin/env python3
# -*- coding: UTF-8 -*-
import re

import pysnooper

from footlbolib.AdPosition.AdPositionAPI import modeladInfo
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon

from footlbolib.testcase import FootlboTestCase

class adPostion(FootlboTestCase):
    '''
    新建AdPostion--查询AdPostion已存在，且信息一致,得到该AdPostion的AdPostionadInfoID--修改信息--确认信息已被修改--删除AdPostion--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = modeladInfo()

    @pysnooper.snoop()
    def run_test(self):

        baseGo = modeladInfo()
        modelNew = baseGo.nameRandom()
        modelNameUpdate = baseGo.nameRandom()
        baseGo.creatID(modelNew)
        res  = baseGo.FindID()
        modelId = res["data"]["list"][0]["id"]
        findNewRes = baseGo.AccurateSearch(modelId)
        self.assert_("创建model是否成功", findNewRes["data"]["code"] == modelNew)
        self.log_info("成功创建model名称:%s,modelID:%s" % (modelNew, modelId))

        baseGo.update(modelId,modelNameUpdate)
        findNewRes = baseGo.AccurateSearch(modelId)
        self.assert_("修改程序是否成功", findNewRes["data"]["code"] == modelNameUpdate)  # 验证是否修改
        self.log_info("成功执行修改程序,修改指定id的Name")
        #发布
        baseGo.publish(modelId)

        baseGo.delete(modelId)
        # mysqlCon().comMysql("DELETE FROM custom_content_model WHERE model_id = %s" % modelId)
        #验证其数据库知否存在该数据
        resMql = mysqlCon().comMysql("SELECT * FROM ad_position WHERE id = %s" % modelId)
        self.assert_( "指定id是否已经被清理",(len(resMql) == 0))


    def post_test(self):
        pass


if __name__ == '__main__':
    adPostion().debug_run()

