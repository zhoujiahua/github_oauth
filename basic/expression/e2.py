#! /usr/bin/python3

"""
表达式 expression  operator operand
"""

# 从左向右 左结合
# 赋值运算符 右结合
USERNAME = 'jerry'
PASSWORD = '123456'

print('please input username:')
user_name = input()
print('please input password:')
user_pass = input()

if user_name == USERNAME and user_pass == PASSWORD:
    print('success')
else:
    print('fail')


