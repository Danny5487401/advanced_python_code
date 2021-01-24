# cpython2.0 垃圾回收算法一般指采用引用计数
a = 1 # 指向1计数 +1
b = a # 指向1计数 +1
del a # 计数-1
print(b)

c = object()
d = c
del c
print(d)

class A:
    #回收对象
    def __del__(self):
        pass

