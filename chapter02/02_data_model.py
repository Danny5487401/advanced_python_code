# 魔法函数 是数据模型的一种概念

class Company:
    def __init__(self,employee_list):
        self.employee = employee_list

    # def __getitem__(self, item):
    #     # item是索引
    #     return self.employee[item]

    def __len__(self):
        return len(self.employee)


company = Company(["danny","tom","joy"])
# len首先调用__len__函数，再调用__getitem__
print(len(company))