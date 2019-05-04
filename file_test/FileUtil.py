# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang
def read():
    with open('demo.txt', 'r') as fl:
        print fl.read()

def readlines():
    with open('demo.txt', 'r') as fl:
        for line in fl.readlines():
            print line.strip()

def writeFile():
    with open('write.txt','w') as fl:
        fl.write("hello world\n")
        fl.write("I love you\n")

def appendFile():
    with open('write.txt','a') as fl:
        fl.write("hello world\n")
        fl.write("I love you\n")

