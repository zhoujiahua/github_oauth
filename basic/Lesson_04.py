#! /usr/bin/python3

'''
Python 面向对象
对象集成性
'''


class Person:
    # 类变量
    MAC = 'Hi static'

    # 构造函数
    def __init__(self, name, age):
        # 实例变量
        self.__count = 0
        self.name = name
        self.age = age

    # 实例方法
    def run_homework(self, info):
        print(self.name, info)


class Student(Person):
    def __init__(self, name, age):
        super(Student, self).__init__(name, age)


student = Student('Tom', 20)
student.run_homework('English')
