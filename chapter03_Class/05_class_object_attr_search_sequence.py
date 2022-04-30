# mro顺序  C3算法

class A:
    name = "A"

    def __init__(self):
        self.name = "obj"


a = A()
print(a.name)  # 由下而上
print()


# 菱形
class D:
    pass


class B(D):
    pass


class C(D):
    pass


class E(B, C):
    pass


print(
    E.__mro__)  # (<class '__main__.E'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)


class E:
    pass


class F(E):
    pass


class G:
    pass


class H(G):
    pass


class J(F, H):
    pass


print(
    J.__mro__)  # (<class '__main__.J'>, <class '__main__.F'>, <class '__main__.E'>, <class '__main__.H'>, <class '__main__.G'>, <class 'object'>)
