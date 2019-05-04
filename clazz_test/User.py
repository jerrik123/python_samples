# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang

'''
   包名最好不要和里面的class名字相同
'''
class User(object):
    '用户个数计数器'
    U_COUNT = 0

    def __init__(self, id, name, age):
        self.id = id
        self.name = name
        self.age = age
        User.U_COUNT += 1

    def getTotalUserCnt(self):
        return User.U_COUNT

    def _printUserInfo(self):
        print "id: %d,name is: %s" % (self.id, self.name)

    def obj2json(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age
        }
