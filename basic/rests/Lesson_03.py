#! /usr/bin/python3

'''
Python 面向对象
方法和函数的区别 方法 偏于设计 函数 面向过程
数据成员
类和对象关系
'''


class Student:
    # 类变量
    MAC = 'Hi static'

    # 构造函数
    def __init__(self, name, age):
        # 实例变量
        self.__count = 0
        self.name = name
        self.age = age

    # 实例方法 关联对象本身
    def print_file(self):
        print(self.name)
        print(self.age)
        print(self.__class__.MAC)
        print(Student.MAC)

    # 类方法 关联类本身
    @classmethod
    def plus_sum(cls):
        cls.MAC = 'Hi Jerry'
        print(cls.MAC)

    # 静态方法 建议少使用与类关联性比较弱
    @staticmethod
    def run_sum():
        print(Student.MAC)
        print('Hi static')

    # 私有方法
    def __run_say(self):
        # 内部调用
        self.print_file()

    def run_marking(self, count):
        if count < 0:
            return '不允许存在负分。'
        self.__count = count
        print('得分：', self.__count)


# 公开的 pubilc 私有的 private

student1 = Student('Hi Tom', 18)
student2 = Student('Hi Jerry', 20)
student1.print_file()
Student.plus_sum()
# student1.plus_sum() # 不推荐这种用法
Student.run_sum()
# student1.run_sum()  # 不推荐这种用法
student1.run_marking(59)
print(student1.__dict__)
Student.__count = 'ok'
print(Student.__count)
