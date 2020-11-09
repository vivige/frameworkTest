#！/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:gww

import unittest
import testsuites
# from testsuites.test_baidu_search import BaiduSearch
# from testsuites.test_get_page_title import GetPageTitle
# from testsuites.test_nba_news_view import ViewLocal
import HTMLTestRunner
import os
import time


# 设置报告文件保存路径
report_path = os.path.dirname(os.path.abspath('.'))+r'/test_report/'
# 获取系统当前时间
now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))

# 设置报告名称格式
htmlFile = report_path+now+'HTMLtemplate.html'


# suite = unittest.TestSuite()
# suite.addTest(BaiduSearch('test_baidu_search'))
# suite.addTest(BaiduSearch("test_search2"))
# suite.addTest(GetPageTitle("test_get_title"))

# 利用makeSuite()方法，一次性加载一个类文件下所有测试用例到suite中去
# suite = unittest.TestSuite(unittest.makeSuite(ViewLocal))
fp = open(htmlFile,'wb')
# 利用discover（）方法去加载一个路径下所有的测试用例。
suite = unittest.TestLoader().discover("testsuites")

# with open(htmlFile,'wb') as fp:


if __name__ == '__main__':
    # runner = unittest.TextTestRunner()
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title="ui测试报告",description="报告如下：",verbosity=2)
    runner.run(suite)
    # runner.run(suite)
    fp.close()