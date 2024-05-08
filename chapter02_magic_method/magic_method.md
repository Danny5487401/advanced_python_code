<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [magic method](#magic-method)
  - [分类](#%E5%88%86%E7%B1%BB)
    - [1. 非数学运算](#1-%E9%9D%9E%E6%95%B0%E5%AD%A6%E8%BF%90%E7%AE%97)
    - [2. 数学运算](#2-%E6%95%B0%E5%AD%A6%E8%BF%90%E7%AE%97)
  - [构造与初始化](#%E6%9E%84%E9%80%A0%E4%B8%8E%E5%88%9D%E5%A7%8B%E5%8C%96)
    - [__new__](#__new__)
  - [类的表示](#%E7%B1%BB%E7%9A%84%E8%A1%A8%E7%A4%BA)
    - [__str__() / __repr__()](#__str__--__repr__)
    - [__bool__()](#__bool__)
  - [访问控制](#%E8%AE%BF%E9%97%AE%E6%8E%A7%E5%88%B6)
  - [比较操作](#%E6%AF%94%E8%BE%83%E6%93%8D%E4%BD%9C)
  - [容器类操作](#%E5%AE%B9%E5%99%A8%E7%B1%BB%E6%93%8D%E4%BD%9C)
  - [可调用对象](#%E5%8F%AF%E8%B0%83%E7%94%A8%E5%AF%B9%E8%B1%A1)
  - [序列化](#%E5%BA%8F%E5%88%97%E5%8C%96)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# magic method


魔法方法：Python 中的类有一些特殊的方法。

在python的类中，以两个下画线__开头和结尾的方法如__new__，__init__ 。这些方法统称“魔术方法”（Magic Method）。
任意自定义类都会拥有魔法方法


使用魔术方法可以实现运算符重载，如对象之间使用 == 做比较时，其实是对象中 __eq__实现的。魔法方法类似于对象默认提供的各种方法



## 分类

python中常见的魔法方法大致可分为以下几类：

* 构造与初始化
* 类的表示
* 访问控制
* 比较操作
* 容器类操作
* 可调用对象
* 序列化

### 1. 非数学运算

* 字符串表示：__repr__,__str__
* 集合，序列相关： __len__,__getitem__,__setitem__,__delitem__,__contains__
* 迭代相关： __iter__,__next__
* 可调用： __call__
* with 上下文管理器： __enter__,__exit__
* 数值转换： __abs__,__bool__,__int__,__float__,__hash__,__index__
* 元类相关，构造与初始化: __new__, __init__
* 属性相关： __getattr__,__setattr__,
        __getattribute__,__setattribute__
        __dir__
* 属性描述符： __get__,__set__,__delete__
* 协程： __await__,__aiter__,__anext__,__aenter__,__aexit__

### 2. 数学运算
* 一元运算符：__neg__，__pos__,__abs__
* 二元运算符：__lt__,__le__,
* 算术运算符：__add__,__sub__
* 反向算术运算符：__radd__,__rsub__
* 增量赋值算术运算符：__iadd__,__isub__
* 位运算符：__invert__ ~ ,__lshift__ <<
* 反向位运算符：__rlshift__
* 增量赋值位运算符：__ilshift__


## 构造与初始化


### __new__
__new__() 场景：我们需要继承内置类时，例如，想要继承 int、str、tuple，就无法使用 __init__ 来初始化了，只能通过 __new__ 来初始化数据


## 类的表示

### __str__() / __repr__()
1. __repr__的目标是准确性，或者说，__repr__的结果是让解释器用的。 
2. __str__的目标是可读性，或者说，__str__的结果是让人看的。

### __bool__()
```python
class Person(object):
    def __init__(self, uid):
        self.uid = uid

    def __bool__(self):
        return self.uid > 10

p1 = Person(4)
p2 = Person(14)
print(bool(p1))  # False
print(bool(p2))  # True
```


## 访问控制

__setattr__：定义当一个属性被设置时的行为

__getattr__：定义当用户试图获取一个不存在的属性时的行为

__delattr__：删除某个属性时调用

__getattribute__：访问任意属性或方法时调用


## 比较操作
比较操作的魔法方法主要包括以下几种：

* __eq__()
* __ne__()
* __lt__()
* __gt__()


## 容器类操作

容器类的魔法方法，主要包括：

* __setitem__(self, key, value)：定义设置容器中指定元素的行为，相当于 self[key] = value；
* __getitem__(self, key)： 定义获取容器中指定元素的行为，相当于 self[key]；
* __delitem__(self, key)：定义删除容器中指定元素的行为，相当于 del self[key]；
* __len__(self)：定义当被 len() 调用时的行为（返回容器中元素的个数）；
* __iter__(self)：定义当迭代容器中的元素的行为；
* __contains__(self, item)：定义当使用成员测试运算符（in 或 not in）时的行为；
* __reversed__(self)：定义当被 reversed() 调用时的行为。

## 可调用对象

Python 中的实例，也是可以被调用的，通过定义 __call__ 方法，就可以传入自定义参数实现自己的逻辑。

## 序列化

Python 提供了序列化模块 pickle，当使用这个模块序列化一个实例化对象时，也可以通过魔法方法来实现自己的逻辑，这些魔法方法包括：

* __getstate__()
* __setstate__()

