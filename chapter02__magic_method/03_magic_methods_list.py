# 非数学运算，数学运算

"""非数学运算
字符串表示：__repr__,__str__
集合，序列相关： __len__,__getitem__,__setitem__,__delitem__,__contains__
迭代相关： __iter__,__next__
可调用： __call__
with 上下文管理器： __enter__,__exit__
数值转换： __abs__,__bool__,__int__,__float__,__hash__,__index__
元类相关: __new__, __init__
属性相关： __getattr__,__setattr__,
        __getattribute__,__setattribute__
        __dir__
属性描述符： __get__,__set__,__delete__
协程： __await__,__aiter__,__anext__,__aenter__,__aexit__
"""


class Company:
    def __init__(self,employee_list):
        self.employee = employee_list

    def __str__(self):
        return "," .join(self.employee)

    def __len__(self):
        return len(self.employee)

    def __repr__(self):
        return "joy"

# len() 函数性能特别高，c语言内部有一个变量维护
company = Company(["danny","tom","joy"])
#<__main__.Company object at 0x00000154129D32C8> 完成__str__ 打印danny,tom,joy
print(company)
print(repr(company))  # 开发模式调用  jupyter 调用  __repr__


"""数学运算
一元运算符：__neg__，__pos__,__abs__
二元运算符：__lt__,__le__,
算术运算符：__add__,__sub__
反向算术运算符：__radd__,__rsub__
增量赋值算术运算符：__iadd__,__isub__
位运算符：__invert__ ~ ,__lshift__ <<
反向位运算符：__rlshift__
增量赋值位运算符：__ilshift__
"""