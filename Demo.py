#!/usr/bin/env python
#-*- coding:utf8 -*-

'''
copyright @wangxiaojie 2020.01.17
author: wangxiaojie
'''

import os, sys

codePath = os.path.abspath(os.path.join(__file__, "..", "Code"))
if os.path.exists(codePath):
    sys.path.append(codePath)
from JsonUtil import *

if __name__ == "__main__":
    #json文件的路径
    jsonFile = os.path.abspath(os.path.join(__file__, "../etc/test.json"))
    
    #获取json文件中的json对象
    result, jsonObj = getJsonFromFile(jsonFile)
    if result:
        print(type(jsonObj))
        print(jsonObj)
    else:
        print("get json error, error msg is %s" % jsonObj)

    #获取json文件中某个键的值
    result = valueFromJsonFile('E', jsonFile)
    if result:
        print(type(result))
        print(result)
    else:
        print("get value error")

    #从json字符串转为json字典
    jsonStr = "{\"A\": \"a\",\"B\": \"b\",\"C\": 0,\"D\": \"d\",\"E\": {\"E1\": \"e1\",\"E2\": \"e2\",\"E3\": 1}}"
    result, jsonObj = getJsonFromStr(jsonStr)
    if result:
        print(type(jsonObj))
        print(jsonObj)
    else:
        print("get json error, error msg is %s" % jsonObj)

    #按键从json字符串获取值
    result = valueFromJsonStr('D', jsonStr)
    if result:
        print(type(result))
        print(result)
    else:
        print("get value error")

    #保存字典到文件
    saveFile = os.path.abspath(os.path.join(__file__, "../etc/save.json"))
    result, msg = saveJsonFile(saveFile, jsonObj)
    if result:
        print(msg)
        print("save json data success")
    else:
        print(msg)
