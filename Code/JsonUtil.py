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
    "ReadJsonFile",
    "SaveJsonFile",
    "GetJsonFromFile",
    "GetJsonFromStr",
    "ValueFromJsonFile"
    ]

def ReadJsonFile(filename):
    try:
        fp = open(filename)
        fp_str = fp.read()
        fp.close()
        if len(fp_str) == 0:
            fp_str = ""
        if fp_str[0] != '{':
            fp_str = "{" + fp_str + "}"
        json_data = json.loads(fp_str)
        return 0, json_data
    except e:
        print("exception is %s" % e)
        return 1, "{0}".format(e)

def SaveJsonFile(filepath, data):
	try:
		finalStr = json.dumps(data, indent=4, ensure_ascii=False).encode("utf8")
		fp = open(filepath, 'w')
		params = fp.write(finalStr)
		fp.close()
	except Exception as err:
		return -1, "{0}".format(traceback.format_exc())
	return 0, "success"

def GetJsonFromFile(filename):
    fp = file(filename)
    if fp == None:
        return None
    jobject = json.load(fp)
    fp.close()
    return jobject 

def GetJsonFromStr(jsonstr):
    jobject = json.loads(jsonstr)
    return jobject

def ValueFromJsonFile(key, filename):
    if not os.path.isfile(filename):
        return False
    jsonParams = GetJsonFromFile(filename)
    if not jsonParams:
        return False
    if key in jsonParams:
        return jsonParams[key]
    return False

if __name__=="__main__":
    jsonFile = os.path.abspath(os.path.join(__file__, "../../etc/test.json"))
    code, result = ReadJsonFile(jsonFile)
    print(result)
    '''
    saveJsonFile = os.path.abspath(os.path.join(__file__, "../../etc/save.json"))
    code, msg = SaveJsonFile(saveJsonFile, result)
    if code != 1:
        print(msg)
        '''
    '''
    str = GetJsonFromFile("../../platform/T4_90146/channels/yishii510/config.json")
    print(str)
    print("str is %s" % str)
    print("run json_util.py")
    '''
   


