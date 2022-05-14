# 判断类型少用type


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        # item是索引  变成可迭代对象
        return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["danny", "tom", "joy"])

# 1. 检查某个类是否有某种方法
print(hasattr(company, "__len__"))
# 判断类型
from collections.abc import Sized

print(isinstance(company, Sized))
print(len(company))




class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))
print(isinstance(b, A))
print(type(b) is B)
print(type(b) == B)
print(type(b) is A)
print(type(b) == A)
# is ID 和 == 数值
