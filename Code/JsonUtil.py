#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.18
author: wangxiaojie
'''

import os,sys
import json
import traceback

__all__ = [
    "getJsonFromFile",
    "getJsonFromStr",
    "valueFromJsonFile",
    "valueFromJsonStr",
    "saveJsonFile"
    ]
          
def getJsonFromFile(filename):
    try:
        fp = open(filename)
        if fp == None:
            return None
        jobject = json.load(fp)
        fp.close()
        return True, jobject 
    except Exception as e:
        print("exception is %s" % e)
        return False, "%s"%e

def getJsonFromStr(jsonstr):
    try:
        jobject = json.loads(jsonstr)
        return True, jobject
    except Exception as e:
        print("exception is %s" % e)
        return False, "%s"%e

def valueFromJsonFile(key, filename):
    if not os.path.isfile(filename):
        return False
    result, jsonParams = getJsonFromFile(filename)
    if not result:
        return False
    if key in jsonParams:
        return jsonParams[key]
    return False

def valueFromJsonStr(key, jsonStr):
    result, jsonParams = getJsonFromStr(jsonStr)
    if not result:
        return False
    if key in jsonParams:
        return jsonParams[key]
    return False
    
def saveJsonFile(filepath, data):
    try:
        finalStr = json.dumps(data, indent=4, ensure_ascii=False).encode("utf8")
        fp = open(filepath, 'bw')
        params = fp.write(finalStr)
        fp.close()
        return True, "success"
    except Exception as e:
        return False, "%s"%e
