# -*- coding: utf-8 -*-"
'''
# Description: 给apache_cae加工cae纬度
# @author: jerrikyang
'''
import sys
import logging
import re
import platform
import MySQLdb

sys.path.append('/data/tools')

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

try:
    from fit_oms import build_request, OmsClient
except Exception as e:
    logger.error("import fit_oms failed")

def getApi_body(ip):
    api_body = {}
    api_body['iplist'] = ip
    return api_body

def query_module_info(ip):
    api_body = getApi_body(ip)
    oms_requst = build_request(service_name="OMS_PROTOCOL_ADAPTOR", api_url="resapi/get_businessInfo_by_ip", body=api_body)
    oms_requst['user'] = 'erwinxiong'
    client = OmsClient("/data/tools/res_tool/conf/oms-client.json")
    oms_response = client.oms_call(oms_requst)
    return oms_response

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
        jdbcConfig = dict(host="...", port=3306, user="...", passwd="...",
                          db="...", charset="GBK")
    else:
        logger.info("init Windows config")
        jdbcConfig = dict(host="...", port=3306, user="...", passwd="...",
                          db="...", charset="GBK")


def getConnection():
    return MySQLdb.Connect(host=jdbcConfig['host'], port=jdbcConfig['port'], user=jdbcConfig['user'],
                           passwd=jdbcConfig['passwd'],
                           db=jdbcConfig['db'], charset=jdbcConfig['charset'])


def readAllIps():
    ip_list = None
    with open('ips.txt', 'r') as file:
        ip_list = file.readlines()

    ip_new_list = []
    for ip in ip_list:
        ip_new_list.append(ip.replace("\n", ""))

    return ip_new_list

mapping = "apache_cae-weixinzhifu-CFT-cgi_sns_pay-fast_cgi:1810004;apache_cae-weixinzhifu-CFT-cgi_sns_pay-slow_cgi:1890003;apache_cae-weixinzhifu-CFT-cgi_biz_pay-fast_cgi:1810001;apache_cae-weixinzhifu-CFT-cgi_biz_pay-slow_cgi:1890001;apache_cae-MobileQQPayment-CFT-cgi_sns_pay-fast_cgi:2750003;apache_cae-MobileQQPayment-CFT-cgi_sns_pay-slow_cgi:2760003;apache_cae-MobileQQPayment-CFT-cgi_biz_pay-fast_cgi:2750001;apache_cae-MobileQQPayment-CFT-cgi_biz_pay-slow_cgi:2760001"

def resolveMap():
    maps = {}
    lists = mapping.split(";")
    for kv in lists:
        arr = kv.split(":")
        maps[arr[0]] = arr[1]
    return maps

moduleMapping = resolveMap()

INSERT_SQL = "replace into cftoss_dimension.module_ext_data(module_type,modulename,ext_type,data_key,data_value,src) values (1,'apache_cae','CAE','%s','%s','CAE_FROM_RES')"

def getFullSQL(ip,data_value):
    return INSERT_SQL %(ip,data_value)

def resolveOmsResponse(omsResponse):
    row = omsResponse['body']['datas'][0]
    bussSet = row['ServiceEngName']
    buss = row['SystemEngName']
    busiName = row['BusiName']
    ip = row['LoginIP']
    moduleName = 'apache_cae'

    key = moduleName + "-" + bussSet + "-" + buss + "-" + busiName
    data_value = moduleMapping[key]

    print "ip: %s, key: %s, data_value: %s" %(ip,key,data_value)

    conn = None
    cursor = None
    try:
        conn = getConnection()
        cursor = conn.cursor()
        cursor.execute(getFullSQL(ip,data_value))
        conn.commit()
    except Exception as e:
        logging.error("insert failed, %s" % (e.message))
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

if __name__ == "__main__":
    init_db_config()

    ipList = readAllIps()
    for ip in ipList:
        try:
            omsResponse = query_module_info(ip)
            resolveOmsResponse(omsResponse)
        except Exception as e:
            logging.error("resolveOmsResponse failed, %s" % (e.message))
    logger.info("completely")
    sys.exit(-1)
