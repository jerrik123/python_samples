# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang
import logging

logger = logging.getLogger()

#日志级别
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")

fileHandler = logging.FileHandler('file.log')
fileHandler.setFormatter(formatter)

#handler的日志级别;file.log只记录ERROR以上的日志
fileHandler.setLevel(logging.ERROR)

consoleHandler = logging.StreamHandler()
consoleHandler.setFormatter(formatter)

#console只记录INFO级别以上的日志
consoleHandler.setLevel(logging.DEBUG)

logger.addHandler(fileHandler)
logger.addHandler(consoleHandler)

logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
