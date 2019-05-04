# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang

import clazz_test.User
import json

from clazz_test.Person import Chinese, America


def jsonFormat(obj, function=None):
    '''json格式化'''
    return json.dumps(obj, ensure_ascii=False, indent=4, default=function)


name_list = ['jerrik', 'bluceli', 'obma']

print json.dumps(name_list)
address = {'id': 3, 'province': '广东省', 'city': 'SZ', 'district': '南山'}

# 如果不设置ensure_ascii=False,则会输出unicode编码
print "json.dumps(dict): %s" % json.dumps(address, ensure_ascii=False, indent=4)

# json格式化class
u = clazz_test.User.User(3, 'jerrik', 32)

print "u.obj2json.__func__: %s" % u.obj2json.__func__

# 手动指定obj转json函数
print json.dumps(u, ensure_ascii=False, indent=4, default=u.obj2json.__func__)

# 转成字典的方式
print "lambda dumps: %s" % json.dumps(u, ensure_ascii=False, sort_keys=True, indent=4, default=lambda obj: obj.__dict__)

chinese = Chinese('32')
print "Chinese dumps: %s" % json.dumps(chinese, ensure_ascii=False, sort_keys=True, indent=4,
                                       default=lambda obj: obj.__dict__)
