
# object


## 对象的特征: 主要身份，类型，值
1. 身份：每个对象在内存中都有个具体的位置（可以用id函数来获得）
2. 类型：对应静态类型,每个对象有一个确定的类型. 例如对象2的类型是 int ，对象 "joe" 的类型是 string.

类型：数值，迭代类型，序列类型，映射（dict)，集合，上下文管理器，None(全局只有一个）

- 数值：int,float,complex复数，bool
- 迭代类型: 迭代器，生成器
- 序列类型：list,bytes,bytearray,memoryview(二级制序列),range,tuple,str,array
- 映射：dict
- 集合：set, frozenset
- 上下文管理类型 with
- 其他，深入python源码： 模块类型，class和实例，函数类型，方法类型，代码类型，object对象，type类型，ellipsis类型，notimplemented类型

3. 有值 - 对象可能包含一堆属性 (i.e. 比如可以通过 objectname.attributename获得其他对象)

4. 


## 参考资料
1 [Python 类型和对象](https://wiki.woodpecker.org.cn/moin/PyTypesAndObjects)