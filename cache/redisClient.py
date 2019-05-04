#!/usr/bin env python
# -*- coding: utf-8 -*-"
'''
# redis cluster操作工具.
#Usage: redisClient.py set hello world
#       redisClient.py get hello
# @author: jerrikyang"
'''

from rediscluster import StrictRedisCluster
from exception import InitialException
import sys
import logging
import sys
import os
import socket

pro_startup_nodes = [

]

test_startup_nodes = [

]

local_ip = "xx"


def getLocalIp():
    '''
        获取本机IP
    '''
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip


def init_cluster():
    try:
        if local_ip == getLocalIp():
            startup_nodes = test_startup_nodes
        else:
            startup_nodes = pro_startup_nodes

        cluster = StrictRedisCluster(startup_nodes=startup_nodes, password="cftadmin", decode_responses=True)
        return cluster;
    except Exception as e:
        logging.error("初始化redis cluster失败")
        raise InitialException(-1, e.message)


def getAutoPlaceHolderOfCluster(argsLength):
    '''
        动态获取redis cluster的占位符
    '''
    if (argsLength == 1):
        raise Exception("参数不能为空")
        sys.exit(-1)
    mExpression = "'%s'," * (argsLength - 2)
    mExpression = mExpression[0:-1]
    return "cluster.%s(" + mExpression + ")"


def resolveParamAndExecuteCmd(argv):
    placeHolder = getAutoPlaceHolderOfCluster(len(argv))
    expression = placeHolder % tuple(argv[1:])
    print expression + ": "
    executeCmd(expression)


def executeCmd(expression):
    cluster = init_cluster()
    try:
        print eval(expression)
    except Exception as e:
        print "执行redis命令失败,message is: %s" % e.message


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print "参数不能为空"
        sys.exit(-1)
    resolveParamAndExecuteCmd(sys.argv)
    sys.exit(-1)
