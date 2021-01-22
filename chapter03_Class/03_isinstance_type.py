# 判断类型少用type

class A:
    pass

class B(A):
    pass


b = B()
print(isinstance(b,B))
print(isinstance(b,A))
print(type(b) is B)
print(type(b) is A)
# is ID 和 == 数值