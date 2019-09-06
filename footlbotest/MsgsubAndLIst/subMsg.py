#!user/bin/env python3
# -*- coding: UTF-8 -*-
import time

import pysnooper
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.Messagae.leaveMsgAPi import  modelMsgInfo

from footlbolib.testcase import FootlboTestCase

class modelSubmsg(FootlboTestCase):
    '''
    新建message--查询message已存在，且信息一致,得到该message的messageadInfoID--修改信息--确认信息已被修改--删除message--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"

    def pre_test(self):
        self.baseGo = modelMsgInfo()

    @pysnooper.snoop()
    def run_test(self):

        baseGo = self.baseGo
        modelNew = baseGo.nameRandom()
        baseGo.creatID(modelNew)
        res  = baseGo.FindID()
        # self.log_info(res)
        modelId = res["data"]["list"][0]["id"]
        self.log_info("该信息的id：%s"%modelId)
        tel = res["data"]["list"][0]["tel"]
        self.log_info(baseGo.phone(tel))
        self.comparsion("该手机号已经被加密","错误的手机号"==baseGo.phone(tel))

        baseGo.delete(modelId) #删除
        time.sleep(2)

        #验证其数据库知否存在该数据
        resMql = mysqlCon().comMysql("SELECT * FROM message where id = %s" % modelId)
        self.comparsion( "指定id是否已经被清理",(len(resMql) == 0))


    def post_test(self):
        pass


if __name__ == '__main__':
    modelSubmsg().debug_run()

