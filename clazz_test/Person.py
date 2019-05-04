# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang
import logging

logging.basicConfig(filename='person.log', level=logging.INFO,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class Chinese(object):
    def __init__(self,id):
        logger.info("Chinese init")
        self.id = id
        pass


class America(object):
    def __init__(self):
        logger.info("America init")
        pass
