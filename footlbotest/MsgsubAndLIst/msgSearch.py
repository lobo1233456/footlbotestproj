#!user/bin/env python3
# -*- coding: UTF-8 -*-
import time

import pysnooper
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.Messagae.leaveMsgAPi import  modelMsgInfo

from footlbolib.testcase import FootlboTestCase

class modelSubmsg(FootlboTestCase):
    '''
    新建message--查询message已存在，且信息一致,得到该message的messageadInfoID--通过姓名
    详情名称
    URL
    页面Title
    地址
    IP
    站点
    房屋类型 装修时间 更新时间
    点击该框选择时间段
    屏蔽 转移
    面积
    查找
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
        self.log_info(res)
        modelId = res["data"]["list"][0]["id"]
        self.log_info("该信息的id：%s"%modelId)
        baseGo.delete(modelId) #删除
        time.sleep(2)

        #验证其数据库知否存在该数据
        resMql = mysqlCon().comMysql("SELECT del_flag FROM message where id = %s" % modelId)
        self.assert_( "指定id是否已经被清理,flag已更改为1",(resMql[0][0] == 1))
        #清理数据库测试数据
        mysqlCon().comMysql("delete FROM message where id = %s" % modelId)



    def post_test(self):
        pass


if __name__ == '__main__':
    modelSubmsg().debug_run()

