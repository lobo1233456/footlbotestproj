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

    def post_test(self):
        pass


if __name__ == '__main__':
    reviewCase().debug_run()

