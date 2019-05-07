# -*- coding: UTF-8  -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang

x = None
if x is None:
    print 'X is None'

print '------'

#False
ele_list = []
if ele_list:
    print True
else:
    print False

print '------'

str = ""
if str:
    print True
else:
    print False

print '------'

#True
if 1:
    print True

print '------'

#False
if 0:
    print True
else:
    print False

print '------'

#True
if -1:
    print True
else:
    print False

print '------'

#False
if None:
    print True
else:
    print False