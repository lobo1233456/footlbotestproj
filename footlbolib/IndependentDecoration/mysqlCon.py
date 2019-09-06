#!/usr/bin/python3

import pymysql

# 打开数据库连接
class mysqlCon():
   def __init__(self):
      self.serverIp = '192.168.2.45'
      self.username = 'root'
      self.port = 3306
      self.password = 'testuser'
      self.dataChart =  "fy_cms"
      self.db = pymysql.connect(host=self.serverIp, port=self.port,user=self.username, passwd = self.password,database='fy_cms')
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
      try:
         # 执行SQL语句
         cursor.execute(sql)
         results = cursor.fetchall()
         db.commit()
         print(results)

      except Exception as e:
         print("Error: unable to fetch data")
         db.rollback()
      # 关闭连接
      db.close()
      return results

if __name__ == '__main__':
   modelId= 64
   # print(mysqlCon().comMysql("SELECT model_id FROM sys_model order by model_id DESC LIMIT 1"))
   # resMql = mysqlCon().comMysql("SELECT * FROM custom_page WHERE page_id = %s" % pageId)


   resMql = mysqlCon().comMysql("SELECT * FROM ad_position WHERE id = %s" % modelId)
   print(resMql)
   #SELECT * FROM ad_position where id = 65
   # existNameList = mysqlCon().delete('test1565578423')
   # print(mysqlCon().searchMysql())

   # nameList = {'tanli2', 'test15646623280'}
   # existNameList = set(existNameList)
   # if len(existNameList & nameList) == 0 :nodifference = True
   #
   # sql ="DELETE   FROM sys_manager WHERE manager_name = 'test1565342096'"


