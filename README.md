
# ***Python高级编程***
**python3.7**
---
![高级ython](https://ss3.bdstatic.com/70cFv8Sh_Q1YnxGkpoWK1HF6hhy/it/u=1443427057,959339510&fm=26&gp=0.jpg)
## 第一章：一切皆对象

1. 函数和类都是对象
2. type是一个类，同时type也是一个基类
3. 对象三个特征:身份，类型，值
---
## 第二章：魔法方法
1. __getitem__实现支持切片
2. len()调用：首先调用__len__函数，再调用__getitem__
3. 魔法方法分类:非数学运算，数学运算
4. 类初始化：先__init__,再__enter__
---
## 第三章：面向对象编程
1. 鸭子类型  
2. 抽象基类  
3. 类变量、对象变量的查找顺序     
4. 静态方法、类方法、实例方法     
5. 数据封装和私有属性     
6. 对象的自省机制   
7. 上下文管理器    
8. contextlib实现上下文管理器    
9. super函数的查找顺序,mixin继承模式的应用
10. with用法
11. @contextlib.contextmanager用处
---
## 第四章：数据结构sequence
1. 序列类分类
2. 可变与不可变序列类魔法方法
3. append和extend
4. 类实现slice
5. bisect有序序列
6. python重写c语言的array
7. 列表,集合,字典推导式
---
## 第五章：数据结构集合和字典
1. mapping类型
2. dict.fromkeys()和dict.setdefault()
3. UserDict继承, defaultdict和OrderedDict
4. set与frozenset
5. dict性能远高于list
---
## 第六章：变量，参数及垃圾回收机制
1. Python变量实际是一个指针
2. ==与is区别
3. GC垃圾回收
4. 传递list的经典错误
5. 不定长参数args与kwargs
---
## 第七章：元类
1. property动态属性
2. __getattr__、__getattribute__区别
3. 属性描述符
4. __new__和__init__
5. 元类metaclass控制实例化过程,动态创建类,type生成类
6. 元类实现ORM
---
## 第八章：迭代器及生成器
1. 迭代协议__iter__与迭代器
2. 可迭代对象Iterator
3. 生成器
4. 底层函数工作原理
5. 生成器读取大文件
---
## 第九章：多进程多线程
1. GIL和多线程
2. 线程通信-共享变量、Queue
3. 线程同步-Lock、RLock、Condition、Semaphor
4. 线程池和源码分析-ThreadPoolExecutor
5. 多进程-multiprocessing
6. 进程间通信
---
## 第十章：IO模型
1. IO多路复用-select、poll、epoll
2. select+回调+事件循环模型
3. 生成器进阶-send、close、throw和yield from
4. async和await
---
## 第十一章：协程库Asyncio
1. 事件循环
2. 协程嵌套coroutine_nest
---
## 第十二章：函数回调及装饰器
1. 回调函数
2. 装饰器基本使用
3. 装饰器语法糖@
4. 装饰器应用
5. 装饰器高级：带参与不带参，返回值与无返回值
6. 类装饰器
---
## 第十三章：责任链编程
1. 设计模式之责任链编程一：未优化代码
2. 设计模式之责任链编程二：优化代码
---
