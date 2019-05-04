# -*- coding: utf-8 -*-"
''',
# Created on  :",
# ",
# @author: jerrikyang",
'''

class InitialException(Exception):
    def __init__(self,code,message):
        self.code = code
        self.message = message