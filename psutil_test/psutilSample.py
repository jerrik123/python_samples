# -*- coding: utf-8 -*-
# @Desc: 程序发布
# @Author: jerrikyang
# @Date:   2018-12-27
# @Last Modified by:   jerrikyang
import psutil

print psutil.os
print psutil.boot_time()
print psutil.cpu_count()
print psutil.disk_usage("D:")
print psutil.cpu_stats()

def printCpuLoadAverage():
    for x in range(10):
        print psutil.cpu_percent(interval=1, percpu=True)



