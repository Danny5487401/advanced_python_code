# 属性描述符
"""查找过程：
如果user 是某个类的实例，那么user.age(以及等价的getattr((user,"age"))
首先调用__getattibute__,
如果类定义了__getattr__方法，那么在_getattribute__抛出AttributeError会调用__getatttr__,
而对于描述符(__get__)的调用，则是发生在__getattribute__内部的，
user = User(),那么user.age顺序如下：
1.如果"age"是出现在类User或者其基类的__dict__中，且age 是data descriptor,那么调用其__get__
2.如果"age"是出现在对象user的__dict__中，那么直接返回obj.__dict__["age"]
3.如果"age"是出现在类Userd或者其基类的__dict__中:
    3.1  如果age是non-data descriptor,那么调用其__get__方法
    3.2  如果不是，调用__dict__["age"]
4.最后如果User有__getattr__方法，调用__getattr__方法，否则调用AttributeError
"""
import numbers
from datetime import date, datetime


# 类型检查,完成get,set_delete魔法方法
class IntField:
    # 数据描述符
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError("int value need")
        # 保存值
        if value < 0:
            raise ValueError("POSITIVE value needed")
        # 如果instance.age 会死循环
        self.value = value

    def __delete__(self, instance):
        pass


# 属性描述符
class NonDataIntFied:
    # 非数据属性描述符
    def __get__(self, instance, owner):
        pass


class User:
    # 属性描述符对象
    age = IntField()
    # age = NonDataIntFied()


# 数据库中的表对应类
# class User:
#     def __init__(self, name, email, birthday):
#         self.name = name
#         self.birthday = birthday
#         # 不像对外暴露，只是规范而已
#         self._age = 0
#         self.email = email
#
#     # 获取年龄 方法一
#     # def get_age(self):
#     #       return datetime.now().year - self.birthday.year
#
#     #方法二 获取年龄
#     # 属性描述符
#     @property
#     def age(self):
#         return datetime.now().year - self.birthday.year
#
#     @age.setter
#     def age(self,value):
#         # 检查是否是字符串类型
#         self._age = value

if __name__ == "__main__":
    user = User()
    # user.age = 30
    user.__dict__["age"] = 33
    print(user.__dict__)
    print(user.__dict__["age"])
    # . 取属性 注意查找顺序
    # print(user.age)
    # print(getattr(user,"age"))
