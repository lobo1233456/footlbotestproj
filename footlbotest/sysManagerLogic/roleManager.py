#!user/bin/env python3
# -*- coding: UTF-8 -*-
from footlbolib.IndependentDecoration.roleApi import roleInfo
from footlbolib.testcase import FootlboTestCase
class roleManager001(FootlboTestCase):
    '''
    新建角色--查询角色已存在，且信息一致,得到该角色的roleID--修改信息--确认信息已被修改--删除角色--确认已经删除
    '''
    owner = "liubo"
    timeout = 5
    priority = FootlboTestCase.EnumPriority.High
    status = FootlboTestCase.EnumStatus.Design
    tags = "BYT"
    def pre_test(self):
        
        self.baseGo = roleInfo()
        # ------------获得随机名字---------------
        self.newName = self.baseGo.nameRandom()
    def run_test(self):
        baseGo = self.baseGo
        responseCreat = baseGo.creatID(self.newName)#创建随机账号
        self.assert_("创建账号:%s是否成功"%self.newName, responseCreat[0]["msg"] ==  '执行成功')
        roleName = baseGo.FindID(self.newName)["data"]["list"][0]["roleName"]
        self.log_info("roleName:%s" % roleName)
        roleId = baseGo.FindID(self.newName)["data"]["list"][0]["roleId"]
        self.log_info("roleId:%s" % roleId)
        #调用查找接口查询该账号是否已经创建
        if (roleName == self.newName) == True:
            self.log_info("nameNew:%s创建成功" % self.newName)
        else:
            raise ("nameNew:%s未创建成功" % self.newName)
        self.changeName = baseGo.nameRandom()
        changeName = self.changeName
        self.log_info("创建新的随机账号名称%s"%changeName)
        baseGo.update(roleId, roleName=changeName)  # 修改roleName
        self.log_info("roleID:%s的名字已经由%s修改为%s" % (roleId, self.newName, changeName))
        data = baseGo.FindID(self.newName)
        self.assert_("检查newName是否还存在",len(data['data']['list'])==0)
        self.roleIdChange = baseGo.FindID(changeName)["data"]["list"][0]["roleId"]
        self.log_info("通过修改后的名字索引roleID:%s" % self.roleIdChange)
        self.assert_("检查newName的roleid是否和之前一致",self. roleIdChange == roleId)

    def post_test(self):
        # 通过该roleID删除该角色
        resDel=self.baseGo.delete(self.roleIdChange)
        self.assert_("检查%s是否已经被清理"%self.roleIdChange, resDel['msg'] == "执行成功")
        self.log_info("roleID:%s已经被清理" % self.roleIdChange)
        enp= self.baseGo.FindID(self.changeName)
        self.assert_("检查changeName是否还存在", len(enp['data']['list']) == 0)


if __name__ == '__main__':
    roleManager001().debug_run()


