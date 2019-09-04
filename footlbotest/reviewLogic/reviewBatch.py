#!user/bin/env python3
# -*- coding: UTF-8 -*-

import pysnooper
import settings
from footlbolib.IndependentDecoration.mysqlCon import mysqlCon
from footlbolib.Review.review_reviews_api import reviewInfo
from footlbolib.testcase import FootlboTestCase

class reviewCase(FootlboTestCase):
    '''
    批量创建评论---批量删除评论
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
        #上传文件至网页端目录
        enpPath = baseGo.upfilisBatch(settings.PROJECT_ROOT_DIR + r"\resources\FIles\pingLun.xlsx")
        #上传评论到网页
        res = baseGo.importDo(enpPath)
        self.comparsion("批量创建评论",res["msg"] =="执行成功")
        #清理data数据，以test开头的评论
        sql = 'DELETE FROM review_reviews WHERE content LIKE "test%"'
        mysqlCon().comMysql(sql)
        pass

    def post_test(self):
        pass


if __name__ == '__main__':
    reviewCase().debug_run()

