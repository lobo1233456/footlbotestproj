#!/usr/bin/python3

import pymysql

# 打开数据库连接
class mysqlCon():
   def __init__(self):
      self.serverIp = '60.205.200.186'
      self.username = 'testuser'
      self.password = '@Fortest'
      self.dataChart =  "fy_cms"
      self.db = pymysql.connect("%s" % self.serverIp, "%s" % self.username, "%s" % self.password, "fy_cms")
      # 使用cursor()方法获取操作游标
      self.cursor = self.db.cursor()

   def searchMysql(self):
      cursor = self.cursor
      db = self.db
      existName = []
      # SQL 查询语句
      sql = "SELECT  manager_name  FROM sys_manager"
      try:
         # 执行SQL语句
         cursor.execute(sql)
         # 获取所有记录列表
         results = cursor.fetchall()

         for i in range(len(results)):
            nameEnp = results[i][0]
            existName.append(nameEnp)

      except:
         print("Error: unable to fetch data")
         db.rollback()
      # 关闭连接
      db.close()
      return existName
   def existName(self,existNameList,nameList):
      '''
       判断该列表中的账号在数据库中存在
      :param nameList: 账号列表
      :return: 存在则为false,不存在则为true
      '''
      nodifference = False
      existNameList,nameList = set(existNameList),set(nameList)
      if len(existNameList & nameList) == 0: nodifference = True
      return nodifference
   def delete(self,name):
      '''
      :param name: str,要删除的名字
      :return: 返回当前的名单
      '''
      cursor = self.cursor
      db = self.db
      # SQL 查询语句
      # name = 'test1565340435'
      sql = "DELETE FROM sys_manager WHERE manager_name = '%s'"%(name)
      try:
         # 执行SQL语句
         cursor.execute(sql)
         # 提交修改
         db.commit()
      except:
         # 发生错误时回滚
         db.rollback()
      # 关闭连接
      db.close()
      return
   def comMysql(self,sql):
      '''
         通用的sql格式
      :param sql: sql搜索语句
      :return: 语句返回的结果
      '''
      cursor = self.cursor
      db = self.db
      existName = []
      # SQL 查询语句
      # sql = "SELECT  manager_name  FROM sys_manager"
      try:
         # 执行SQL语句
         cursor.execute(sql)
         # 获取所有记录列表
         results = cursor.fetchall()
         # for i in range(len(results)):
         #    nameEnp = results[i][0]
         #    existName.append(nameEnp)
         db.commit()

      except:
         print("Error: unable to fetch data")
         db.rollback()
      # 关闭连接
      db.close()
      # return results

if __name__ == '__main__':
   print(mysqlCon().comMysql("SELECT model_id FROM sys_model order by model_id DESC LIMIT 1"))
   #
   # existNameList = mysqlCon().delete('test1565578423')
   # print(mysqlCon().searchMysql())

   # nameList = {'tanli2', 'test15646623280'}
   # existNameList = set(existNameList)
   # if len(existNameList & nameList) == 0 :nodifference = True
   #
   # sql ="DELETE   FROM sys_manager WHERE manager_name = 'test1565342096'"

