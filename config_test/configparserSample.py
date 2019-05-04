# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang
from configparser import ConfigParser

parser = ConfigParser()
parser.read('mysql.ini')

sections = parser.sections()
print "sections is: %s,type is: %s" % (sections,type(sections))

options = parser.options('mysql')
print "options is: %s,type is: %s" % (options,type(options))

items = parser.items('mysql')
print "items is: %s,type is: %s" % (items,type(items))

print "mysql host: %s" %parser.get('mysql','host')
print "mysql port: %s" %parser.get('mysql','port')