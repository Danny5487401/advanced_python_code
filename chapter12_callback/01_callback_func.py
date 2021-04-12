"""
将函数作为参数传递给另一个函数，一共分为4种情况：

1. 将普通函数传递给普通函数
2. 将普通函数传递给类成员函数
3. 将类成员函数传递给普通函数
4. 将类成员函数传递给类成员函数

"""


# !/usr/bin/python3

class Person:
    def __init__(self):
        pass

    def callback(self, data, param=None):
        print(self.__class__.__name__ + " callback:")
        print("data: " + str(data))
        print("param: " + str(param))

    def do_call_func(self, func, data, param=None):
        print(self.__class__.__name__ + " do_call_func:")
        func(data, param)

    def do_call_class_func(self, func, data, obj, param=None):
        print(self.__class__.__name__ + " do_call_class_func:")
        func(obj, data, param)


def mycallback(data, param=None):
    print("data: " + str(data))
    print("param: " + str(param))


def do_call_func(func, data, param=None):
    func(data, param)


def do_call_classfunc(func, data, obj, param=None):
    func(obj, data, param)


person = Person()

# common func as callback pass to common func
# 1. 将普通函数传递给普通函数
do_call_func(mycallback, "danny1", "xxx")

# common func as callback pass to class func
# 2.将普通函数传递给类成员函数
person.do_call_func(mycallback, "danny2")

# class func as callback pass to common func
# 3. 将类成员函数传递给普通函数
do_call_classfunc(Person.callback, "danny3", person, None)

# class func as callback pass to class func
# 4. 将类成员函数传递给类成员函数
person.do_call_class_func(Person.callback, "44444444", person, None)
