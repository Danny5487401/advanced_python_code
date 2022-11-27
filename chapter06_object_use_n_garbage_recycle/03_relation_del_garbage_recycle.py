# cpython2.0 垃圾回收算法一般指采用引用计数
# 垃圾回收机制主要是以引用计数为主要手段，以标记清除和分代回收机制作为辅助手段实现的。
"""
我们都知道Python一种面向对象的脚本语言，对象是Python中非常重要的一个概念。在Python中数字是对象，字符串是对象，任何事物都是对象，而它们的核心就是一个结构体--PyObject。
看源码：// include/object.h

typedef struct _object {
    _PyObject_HEAD_EXTRA
    Py_ssize_t ob_refcnt;
    struct _typeobject *ob_type;
} PyObject;

typedef struct _object {
    PyObject_HEAD
} PyObject;

从上方官方注释理解一下，就是说这个PyObject是在C实现中所有Object的基类（不过基类这种解释并不准确，这是纯C语言）。
    要注意的是，它并不是我们在python中的object类，因此，我们在Python中是找不到与之对应的对象的.
    英文注释中写了很重要的一句：This is inheritance built by hand。就是说其他Python对象是可以继承这个PyObject的，但是这又是C，因此需要Python开发者手动操作


typedef struct {
    PyObject_VAR_HEAD
} PyVarObject;

PyVarObject是Python中可变长度的对象的基类，比如python中的list。而PyObject则是定长对象的基类，比如python中的int。

细读PyVarObject的定义可以发现，按照上面记录的手动继承逻辑，PyVarObject就是PyObject的子类

"""
import sys
a = 100 # 指向100计数 +1
print(sys.getrefcount(a))  # 9

#  注意： 这里实际上100这个对象并没有在内存中新建，因为在Python启动解释器的时候会创建一个小整数池，在-5~256之间的整数对象会被自动加载到内存中等待调用。
b = a # 指向1计数 +1
print(sys.getrefcount(a))  # 10
print(sys.getrefcount(b))  # 10
del a  # 计数-1
print(sys.getrefcount(b))  # 9
# 记住引用的变量a、b指向的是数据100，而不是变量本身


c = object()
d = c
del c


class A:
    # 回收对象
    def __del__(self):
        pass

"""引用计数：
优点：引用计数有一个最大的优点，那就是“实时性”，如果这个对象没有引用，内存就直接释放了，而其他垃圾回收技术必须在某种特殊条件下才能进行无效内存的回收。

缺点：无法解决循环引用带来的问题。循环引用可以使一种引用对象的引用计数不为0，然而这些对象实际上并没有被任何外部对象所引用，它们之间只是相互引用，
    这意味着这组对象所占用的内存空间是应该被回收的，但是由于循环引用导致的引用计数不为0，所以这组对象所占用的内存空间永远不会被释放。
    如下，list1与list2相互引用，如果不存在其他对象对它们的引用，list1与list2的引用计数也仍然为1，所占用的内存永远无法被回收，这将是致命的。
    list1 = []
    list2 = []
    list1.append(list2)
    list2.append(list1)
"""

"""标记清除
标记清除算法作为Python的辅助垃圾收集技术，主要处理的是一些容器对象，比如list、dict、tuple等，因为对于字符串、数值对象是不可能造成循环引用问题。
    Python使用一个双向链表将这些容器对象组织起来。不过，这种简单粗暴的标记清除算法也有明显的缺点：
    清除非活动的对象前它必须顺序扫描整个堆内存，哪怕只剩下小部分活动对象也要扫描所有对象
"""

"""分代回收
分代回收是建立在标记清除技术基础之上的，是一种以空间换时间的操作方式。

Python将内存根据对象的存活时间划分为不同的集合，每个集合称为一个代，Python将内存分为了3“代”，分别为年轻代（第0代）、中年代（第1代）、老年代（第2代），
    他们对应的是3个链表，它们的垃圾收集频率与对象的存活时间的增大而减小。新创建的对象都会分配在年轻代，年轻代链表的总数达到上限时，Python垃圾收集机制就会被触发，
    把那些可以被回收的对象回收掉，而那些不会回收的对象就会被移到中年代去，依此类推，老年代中的对象是存活时间最久的对象，甚至是存活于整个系统的生命周期内
"""
