class A:
    aa = 1

    def __init__(self,x,y):
        self.x = x
        self.y = y
        # self.aa = 2


a = A(2,3)
# 修改属性
A.aa = 11
#  a.aa 属性查找方式,实例向上查找
print(a.x,a.y,a.aa) #2 3 11
print(A.aa) # 11

# 给实例添加属性
a.aa =100
print(a.x,a.y,a.aa) # 2 3 100
print(A.aa) # 11

b =A(3,5)
print(b.aa)  # 11  强调添加了实例属性