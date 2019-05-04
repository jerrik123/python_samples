# -*- coding: utf-8 -*-"
''',
# Created on  :",
# ",
# @author: jerrikyang",
'''
import requests
import json

URLS = [
    "http://localhost:8080/home/getOne",
    "http://localhost:8080/home/getOneWithParam?id=3&name=jsdfs",
    "http://localhost:8080/home/postOne"
]

def getRequest():
    response = requests.get(URLS[0])
    print "get response: %s" %response
    print "get response url: %s" %response.url
    print "get response content: %s" % response.content
    print "get response microseconds: %s" %response.elapsed.microseconds
    print "get response headers: %s" %response.headers
    print "get response status_code: %s" %response.status_code
    print "get response text: %s" %response.text
    print "get response reason: %s" %response.reason

def getRequestWithParam():
    print URLS[1]
    #response = requests.get(URLS[1])
    response = requests.get("http://localhost:8080/home/getOneWithParam",{'id':44,'name':'linfeng'})
    print "get response: %s" %response
    print "get response url: %s" %response.url
    print "get response content: %s" % response.content
    print "get response microseconds: %s" %response.elapsed.microseconds
    print "get response headers: %s" %response.headers
    print "get response status_code: %s" %response.status_code
    print "get response text: %s" %response.text
    print "get response reason: %s" %response.reason

def postRequest():
    headers = {'content-type': 'application/json'}
    response = requests.post(URLS[2],json={"id":44,"userName":"linfeng"},headers=headers)

    print "post response: %s" %response
    print "post response url: %s" %response.url
    print "post response content: %s" % response.content
    print "post response microseconds: %s" %response.elapsed.microseconds
    print "post response headers: %s" %response.headers
    print "post response status_code: %s" %response.status_code
    print "post response text: %s" %response.text
    print "post response reason: %s" %response.reason

postRequest()