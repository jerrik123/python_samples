# -*- coding: utf-8 -*-"
'''
# Description: 清除snp_apache server信息
# @author: jerrikyang
'''
import sys
import MySQLdb
import logging
import time
import re
import platform

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


QUERY_SQL = "select id,modulename,type,value from cftoss_dimension.module_dimen where modulename='snp_apache' and type='DST_SERVER'"

DELTE_SQL = "delete from cftoss_dimension.module_dimen where id in (%s)"

#待删除列表
DELETED_list = []

# 每次删除的条数
DELETE_STEP_LEN = 1

# 删除总行数
DELETE_CNT = 0

# 删除一次休眠秒数
SLEEP_SEC = 1

def isIP(str):
    '''
        验证是否为IP
    '''
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False

def init_db_config():
    '''
        根据平台不同初始化DB配置
    '''
    global jdbcConfig
    if platform.system() == "Linux":
        logger.info("init Linux config")
        jdbcConfig = dict(host="xxxx", port=3306, user="xxx", passwd="xxx",
                          db="cftoss_dimension", charset="GBK")
    else:
        logger.info("init Windows config")
        jdbcConfig = dict(host="xxxx", port=3306, user="xxx", passwd="xxx",
                          db="cftoss_dimension", charset="GBK")

def getConnection():
    return MySQLdb.Connect(host=jdbcConfig['host'], port=jdbcConfig['port'], user=jdbcConfig['user'],
                           passwd=jdbcConfig['passwd'],
                           db=jdbcConfig['db'], charset=jdbcConfig['charset'])

def executeDelete(fullSQL):
    '''
        执行DELETE操作
    '''
    cursor = None
    conn = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        row = cursor.execute(fullSQL)
        global DELETE_CNT
        DELETE_CNT = DELETE_CNT + row
        conn.commit()
    except Exception, e:
        conn.rollback()
        logger.error("delete error--%s: " % (e))
    finally:
        cursor.close()
        conn.close()


def doHandle(rowTuple):
    '''
        执行方法
    '''
    id = rowTuple[0]
    value = rowTuple[3]
    if isIP(value):
        DELETED_list.append(id)
        if len(DELETED_list) == DELETE_STEP_LEN:
            executeDelete(getFullSql(DELETED_list))
            del DELETED_list[:]
            logging.info("sleep %s" % SLEEP_SEC)
            time.sleep(SLEEP_SEC)

def getFullSql(element_list):
    '''
        获取完整SQL
    '''
    joinString = joinList(element_list)
    return DELTE_SQL % (joinString)


def joinList(element_list, sep=","):
    '''
        将list按指定符号进行拼接
    '''
    ids = ""
    index = 0
    for id in element_list:
        if index == 0:
            ids = str(id)
        else:
            ids = ids + sep + str(id)
        index = index + 1
    return ids


if __name__ == "__main__":
    init_db_config()
    conn = getConnection()
    cursor = conn.cursor()
    cursor.execute(QUERY_SQL)
    for row in cursor.fetchall():
        try:
            doHandle(row)
        except Exception as e:
            logger.error("doHandle error" + e.message)
    cursor.close()
    conn.close()
    logger.info("completely,delete total num is: %s" % DELETE_CNT)
    sys.exit(-1)
