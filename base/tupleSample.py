# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang

#如果没有逗号,则会认为是int
t = (1,)
print type(t)
print len(t)

def buildKV():
    return ('hello','world')

kv = buildKV()
print type(kv)

a = tuple(x*x for x in range(3))
print a


print "hello " * 3