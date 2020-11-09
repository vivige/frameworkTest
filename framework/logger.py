#！/usr/bin/env python
# -*-coding:utf-8 -*-

#Author:gww

import logging
import os.path
import time
class Logger():
	def __init__(self,logger=None):
		self.logger = logging.getLogger(logger)
		self.logger.setLevel(logging.DEBUG)

		# 	创建handler，写入文件
		rq = time.strftime("%Y%m%d%H%M%S",time.localtime(time.time()))
		file_path= os.path.dirname(os.getcwd())+r'/logs/'
		log_name = file_path+rq+'.log'
		fh = logging.FileHandler(log_name)
		fh.setLevel(logging.INFO)

		# 创建handler，控制台输出
		ch = logging.StreamHandler()
		ch.setLevel(logging.INFO)

		# 定义handler的输出格式
		formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
		fh.setFormatter(formatter)
		ch.setFormatter(formatter)

		# 给logger添加handler
		self.logger.addHandler(fh)
		self.logger.addHandler(ch)

	def getlog(self):
		return self.logger
