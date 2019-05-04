# -*- coding: utf-8 -*-"
''',
# Created on  :",
# ",
# @author: jerrikyang",
'''
import logging

print __name__
logging.basicConfig(level=logging.ERROR,filename="out.log",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

logger.info('This is a log info')
logger.debug('Debugging')
logger.warning('Warning exists')
logger.info('Finish')