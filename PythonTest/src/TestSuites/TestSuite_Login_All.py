#coding=utf-8
'''
Created on 2015年9月2日

@author: QLLU
'''

import HTMLTestRunner
import unittest
import sys,time
import os
reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("..")
sys.path.append(os.getcwd()+"src/")
sys.path.append(os.getcwd()+"/PythonTest/src/")

#引用测试用例文件
from TestCases.QT_Login import testcases_login
from TestCases.QT_Sche import testcases_sche

class testsuit_all():
    
    def test(self):
        if __name__ == "__main__":
   
            #构造测试集
            # suite.addTest(unittest.makeSuite(testcases_login.testlogin(self))) #方法2，类名.方法
            # suite.addTests(unittest.defaultTestLoader.loadTestsFromTestCase(testsuit_all)) #方法3

            suite = unittest.TestSuite() 
            suite.addTest(testcases_login('test_login'))
            suite.addTest(testcases_sche('test_sche'))

            now = time.strftime("%Y%m%dT%H%M%S_",time.localtime(time.time()))
            filename = '../Report/' + now + 'result.html' #测试报告路径

            print filename
            fp = file(filename, 'wb')
            
            #添加测试报告
            runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = 'Result',description = 'Test_Result：') 
            runner.run(suite)  
            
            # 运行测试用例集 
            # runner = unittest.TextTestRunner()
            # runner.run(suite)

if __name__ == "__main__":   
    testsuit_all().test()