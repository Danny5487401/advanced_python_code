class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        # item是索引
        return self.employee[item]


# 魔法方法不是Object的，是自己添加的
company = Company(["danny", "tom", "joy"])
# 方法一
employee = company.employee
for em in employee:
    print(em)

# 方法二   循环对象 for ：先调用iter,后来 __getitem__
# __getitem__  写完支持切片,可以调用len函数
company1 = company[:2]
for em in company1:
    print(em)
