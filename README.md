#JsonUtil
###函数说明

- getJsonFromFile    从json文件中获取整个json对象
- getJsonFromStr     从json字符串获取整个json对象
- valueFromJsonFile  从json文件中按键取值
- valueFromJsonStr   从json字符串中按键取值
- saveJsonFile       保存字典到json文件
-
- getDefaultFromJsonObj    从字典中获取对应键的值，如果没有找到对应键，则返回default键的值，如果连default也没有，则返回None，如果第二个参数传入为非字典，直接返回第二个参数的值
- combineUnitList 合并两个list，并将重复的元素去除
###使用样例
- 详见 Demo.py