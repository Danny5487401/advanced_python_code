"""访问者模式【Visitor】
意图：

1)对象结构中对象对应的类很少改变，但经常需要在此对象结构上定义新的操作。
2)需要对一个对象结构中的对象进行很多不同的并且不相关的操作，而需要避免让这些操作”污染”这些对象的类，也不希望在增加新操作时修改这些类。

适用性：

访问者可以对功能进行统一，可以做报表、UI、拦截器与过滤器。

比如：

安排不同年份的财务报表给不同的角色分析，这就是访问者模式的魅力；访问者模式的核心是在保持原有数据结构的基础上，实现多种数据的处理方法，该方法的角色就是访问者。

"""