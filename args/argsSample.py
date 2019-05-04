# -*- coding: utf-8 -*-"
''',
# Created on  :",
# ",
# @author: jerrikyang",
'''

def test_args(first, second, third, fourth, fifth):
    print 'First argument: ', first
    print 'Second argument: ', second
    print 'Third argument: ', third
    print 'Fourth argument: ', fourth
    print 'Fifth argument: ', fifth

def test_args2(first, second, third=None, fourth=None, fifth=None):
    print 'First argument: ', first
    print 'Second argument: ', second
    print 'Third argument: ', third
    print 'Fourth argument: ', fourth
    print 'Fifth argument: ', fifth

#test_args(3,4,5,5,6)
#test_args2(3,4)

args = [3,2,23,4,1]
test_args(*args)