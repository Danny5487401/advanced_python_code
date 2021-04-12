"""
将函数作为参数传递给另一个函数，一共分为4种情况：

1. 将普通函数传递给普通函数
2. 将普通函数传递给类成员函数
3. 将类成员函数传递给普通函数
4. 将类成员函数传递给类成员函数
Note:如果回调函数是一个类成员函数，那么调用该回调函数时，第一个参数必须是该类的一个对象，
    也就是说，必须将该类的对象，作为一个普通参数，传递给调用该回调函数的函数
"""


# !/usr/bin/python3

class Person:
    def __init__(self):
        pass

    # 方法中最终执行回调的逻辑
    def callback(self, data, param=None):
        print("开始执行类成员回调函数")
        print("类方法是："+self.__class__.__name__ + " callback:")
        print("data: " + str(data))
        print("param: " + str(param))
        print("结束执行类成员回调函数")
        print("\n")

    #类函数中传入普通函数
    def do_call_func(self, func, data, param=None):
        print("类方法是："+self.__class__.__name__ + " do_call_func:")
        func(data, param)

    # 类函数中传入类成员函数
    def do_call_class_func(self, func, data, obj, param=None):
        print("类方法是："+self.__class__.__name__ + " do_call_class_func:")
        func(obj, data, param)



# 普通函数中最终执行回调的逻辑
def my_callback(data, param=None):
    print("开始执行普通回调函数")
    print("普通回调函数中data: " + str(data))
    print("普通回调函数中param: " + str(param))
    print("结束执行普通回调函数")
    print("\n")


def do_call_func(func, data, param=None):
    func(data, param)


def do_call_classfunc(func, data, obj, param=None):
    func(obj, data, param)


person = Person()

# common func as callback pass to common func
# 1. 将普通函数传递给普通函数
do_call_func(my_callback, "danny1", "param1")

# common func as callback pass to class func
# 2.将普通函数传递给类成员函数
person.do_call_func(my_callback, "danny2", "param2")

# class func as callback pass to common func
# 3. 将类成员函数传递给普通函数
do_call_classfunc(Person.callback, "danny3", person, "param3")

# class func as callback pass to class func
# 4. 将类成员函数传递给类成员函数
person.do_call_class_func(Person.callback, "danny4", person, "param4")
