#！/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:gww
from framework.base_page import BasePage

class NewsHomePage(BasePage):
	# 点击国内新闻入口
	local_news = "xpath=>//*[@id='channel-all']/div/ul/li[2]/a"

	def click_local_news(self):
		self.click(self.local_news)
		self.sleep(2)
		self.get_windows_img()