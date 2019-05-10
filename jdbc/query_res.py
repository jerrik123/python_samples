# -*- coding: utf-8 -*-"
'''
# Description: 给apache_cae加工cae纬度
# @author: jerrikyang
'''
import sys
import re

sys.path.append('/data/tools')

try:
    from fit_oms import build_request, OmsClient
except Exception as e:
    print "import fit_oms failed"

def getApi_body():
    api_body = {}
    api_body['iplist'] = '...'
    return api_body

def queryResInfo():
    api_body = getApi_body()
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

if __name__ == "__main__":
    print queryResInfo()
