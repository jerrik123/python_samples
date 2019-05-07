# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang

from threading import Thread
from time import ctime, sleep

def music(args):
    for i in range(2):
        print "I was listening to %s. %s" % (args, ctime())
        sleep(1)


def move(args):
    for i in range(2):
        print "I was at the %s! %s" % (args, ctime())
        sleep(5)


threads = []
t1 = Thread(target=music, args=('爱情买卖',))
threads.append(t1)
t2 = Thread(target=move, args=('阿凡达',))
threads.append(t2)

if __name__ == '__main__':
    for t in threads:
        t.setDaemon(True)
        t.start()

    print "all over %s" % ctime()
