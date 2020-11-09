#！/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:gww
import time
from framework.browser_engine import BrowserEngine
import unittest
from pageobjects.baidu_homepage import HomePage

class BaiduSearch(unittest.TestCase):

	@classmethod
	def setUpClass(cls):
		browse = BrowserEngine(cls)
		cls.driver = browse.open_browser(cls)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()


	def test_baidu_search(self):
		"""
		这里一定要test开头，把测试逻辑代码封装到一个test开头的方法里。
		:return:
		"""
		# self.driver.find_element_by_id('kw').send_keys('selenium')
		# time.sleep(1)
		# try:
		# 	assert 'selenium' in self.driver.title
		# 	print('Test Pass.')
		# except Exception as e:
		# 	print('Test Fail.', format(e))

		homepage = HomePage(self.driver)
		homepage.type_search('selenium')
		homepage.send_submit_btn()
		time.sleep(2)
		homepage.get_windows_img()

		try:
			assert '百度一下' in homepage.get_page_title()
			print("test pass")
		except Exception as e:
			print('Test Fail.', format(e))
	def test_search2(self):
		homepage = HomePage(self.driver)
		homepage.type_search('python')
		homepage.send_submit_btn()
		time.sleep(2)
		homepage.get_windows_img()
if __name__ == '__main__':
	unittest.main()