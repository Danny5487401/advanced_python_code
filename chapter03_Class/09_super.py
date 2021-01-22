# class A:
#     def __init__(self):
#         print("A")
#
#
# class B(A):
#     def __init__(self):
#         print("B")
#         # python 2
#         # super(B,self).__init__()
#         # python3
#         super().__init__()

# super的执行顺序：涉及mro的算法
from threading import Thread
class Mythread(Thread):
    # 父类有name
    def __init__(self,name,user):
        self.user = user
        # self.name = name
        # 调用父类进行验证
        super().__init__(name=name)

class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()

class D(B,C):
    def __init__(self):
        print("D")
        super(D,self).__init__()

if __name__ == "__main__":
    # b = B()
    # 不能理解就调用父类，涉及mro
    d =D()