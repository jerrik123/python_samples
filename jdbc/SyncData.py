# -*- coding: utf-8 -*-"
''',
# Created on  :",
# ",
# @author: jerrikyang",
'''

import MySQLdb
from MySQLdb import connect


def queryTransList():
    conn = connect("xx", "xx", "xxx", "xx", charset='utf8')
    cursor = conn.cursor()
    cursor.execute("select * from t_analysis_flow_trans")
    data = cursor.fetchall()
    print type(data)
    for item in data:
        print type(item)
    conn.close()

queryTransList()
