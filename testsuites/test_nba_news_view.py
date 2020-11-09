#！/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:gww
import unittest
from framework.browser_engine import BrowserEngine
from pageobjects.baidu_homepage import HomePage
from pageobjects.baidu_news_home import NewsHomePage
from pageobjects.baidu_local_home import LocalNewsHomePage
import os.path
import time

class ViewLocal(unittest.TestCase):
	@classmethod
	def setUpClass(cls):
		browse = BrowserEngine(cls)
		cls.driver = browse.open_browser(cls)

	@classmethod
	def tearDownClass(cls):
		cls.driver.quit()
		
	def test_view_views(self):
		# 初始化百度首页，点击新闻链接
		baiduhome = HomePage(self.driver)
		# baiduhome.click_news()
		self.driver.find_element_by_xpath("//*[@id='s-top-left']/a[1]").click()
		baiduhome.get_windows_img()


		windows = self.driver.window_handles
		self.driver.switch_to_window(windows[-1])
		time.sleep(2)

		# 初始化一个百度新闻主页对象，点击国内
		newhome = NewsHomePage(self.driver)

		self.driver.find_element_by_xpath("//*[@id='channel-all']/div/ul/li[2]/a").click()
		newhome.get_windows_img()
		time.sleep(2)

		# 初始化一个国内新闻主页，点击轮播图
		localhome = LocalNewsHomePage(self.driver)
		self.driver.find_element_by_xpath("// *[ @ id = 'imgplayer-next']").click()
		localhome.get_windows_img()
		time.sleep(2)

if __name__ == '__main__':
    unittest.main(verbosity=2)