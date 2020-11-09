#！/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:gww

import configparser
import os.path
from  selenium import webdriver
from framework.logger import Logger

logger = Logger(logger='BrowserEngine').getlog()

class BrowserEngine():
	dir = os.path.dirname(os.path.abspath("."))
	chrome_driver_path = dir+r'/tools/chromedriver.exe'
	def __init__(self,driver):
		self.driver = driver

	def open_browser(self,driver):
		config = configparser.ConfigParser()
		file_path = os.path.dirname(os.path.abspath("."))+r'/config/config.ini'
		config.read(file_path,encoding='utf-8')

		browser = config.get("browserType","browserName")
		logger.info('You had select %s browser' %browser)
		url = config.get("testServer","URL")
		logger.info("the test server url is %s." %url)

		if browser == "Chrome":
			driver = webdriver.Chrome(self.chrome_driver_path)
		else:
			logger.warn("no browser")

		driver.get(url)
		logger.info("Open url %s"%url)
		driver.maximize_window()
		logger.info("Maximize the current window.")
		driver.implicitly_wait(10)
		logger.info("Set implicitly wait 10 seconds.")
		return driver
	def quit_broser(self):
		logger.info("Now, Close and quit the browser.")
		self.driver.quit()


