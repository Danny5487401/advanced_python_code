
"""
单例模式
实现__new__方法
并在将一个类的实例绑定到类变量_instance上,
如果cls._instance为None说明该类还没有实例化过,实例化该类,并返回
如果cls._instance不为None,直接返回cls._instance
"""


class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            # 判断是否有该实例存在,前面是否已经有人实例过，如果内存没有该实例...往下执行
            # 需要注明该父类的内存空间内最多允许相同名字子类的实例对象存在1个（不可多个）
            orig = super(Singleton, cls)  # farther class
            cls._instance = orig.__new__(cls)
        return cls._instance


class MyClass(Singleton):
    def __init__(self, name):
        self.name = name


class ldc(Singleton):
    def __init__(self, name):
        self.name = name


if __name__ == '__main__':
    # 实例化一个类MyClass
    a = MyClass("first class")
    print(a.name)
    # 对类MyClass进行第二次实例化
    b = MyClass("second class")
    print(a.name, b.name)
    # 实例化一个类ldc
    c = ldc('third')
    print(a.name, b.name, c.name)
    print(id(a), id(b), id(c))


"""
总结：
通过执行结果我们可以看出：一个类永远只允许一个实例化对象，不管多少个进行实例化，都返回第一个实例化的对象
"""
