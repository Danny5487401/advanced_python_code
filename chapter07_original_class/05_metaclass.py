# 类也是对象，type创建类的类
from collections import abc


# 什么是，就是创建类的类type
# 必须继承type
class MetaClass(type):
    # 控制生成过程
    def __new__(cls, *args, **kwargs):
        # 注意此参数传递
        return super().__new__(cls, *args, **kwargs)


# 控制实例化的过程，会首先寻找metaclass，包括找基类中的metaclass,通过metaclass去创建User类
# 无metaclass时才type生成类对象
class User(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "user_danny"


# 动态创建类
def create_class(name):
    if name == "user":
        class User:
            def __str__(self):
                return "user"

        return User
    elif name == "company":
        class Company:
            def __str__(self):
                return "company"

        return Company


# 更灵活的写法
# type创建类
"""
        type(object_or_name, bases, dict)
        type(object) -> the object's type
        type(name, bases, dict) -> a new type
        # (copied from class doc)
"""


# User = type("User",(),{})
def say(self):
    return "i am user"
    # return self.name


class BaseClass:
    def answer(self):
        return "i am baseclass"


if __name__ == "__main__":
    # 1. 动态创建类
    # Myclass = create_class("user")
    # my_obj = Myclass()
    # print(my_obj)

    # 2. type创建类
    # 创建属性方法
    # User = type("User", (BaseClass,), {"name":"user","say":say})
    # my_obj = User()
    # print(my_obj.name)
    # print(my_obj.say())
    # print(my_obj.answer())

    # 3. 元类写法
    my_obj = User("danny")
    print(my_obj)
