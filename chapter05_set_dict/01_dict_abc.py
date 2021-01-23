from collections.abc import Mapping,MutableMapping
# dict 属于mapping 类型
print(isinstance(dict,Mapping))
print(isinstance(dict,MutableMapping))
# 用实例判断 dict是类
a = {}
print(isinstance(a,Mapping))  #isinstance 只是说a 实现了Mapping的接口   register注册了dict
print(isinstance(a,MutableMapping))