#！/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:gww

from framework.base_page import BasePage

class LocalNewsHomePage(BasePage):
	local_links = "xpath=>// *[ @ id = 'imgplayer-next']"

	def click_local(self):
		self.click(self.local_links)
		self.sleep(2)
		self.get_windows_img()