#! /usr/bin/python3

'''
JSON 轻量级数据交换格式
易于阅读
易于解析
网络传输效率高
跨语言数据交互
'''

import json

# 序列化 反序列化
json_str = '{"name":"jerry","age":18,"flag":true}'
json_arr = '[{"name":"jerry","age":18,"flag":true},{"name":"jerry","age":18,"flag":false}]'

# JSON数据转换字典
js = json.loads(json_str)
ja = json.loads(json_arr)
print(type(js), js)
print(type(ja), ja)
