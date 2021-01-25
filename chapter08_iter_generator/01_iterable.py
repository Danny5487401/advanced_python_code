# 什么是迭代协议 __iter__
# 迭代器：访问元素的一种方式，遍历数据
# 迭代器与访问下标的访问方式不一样，迭代器不能返回，迭代器是惰性访问数据

# 下标【】list  __getitem__

from collections.abc import Iterable,Iterator
a = list()
b = iter(a)
print(isinstance(a, Iterable))
print(isinstance(b, Iterator))