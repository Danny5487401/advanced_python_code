# 传递list可能会出现莫名其妙的错误

def add(a, b):
    a += b
    return a


class Company:
    def __init__(self, name, staffs=[]):
        self.name = name
        self.staffs = staffs

    def add(self, staff_name):
        self.staffs.append(staff_name)

    def remove(self, staff_name):
        self.staffs.remove(staff_name)


if __name__ == "__main__":
    company = Company("company", ["danny1", "danny2"])
    company.add("danny3")
    company.remove("danny1")
    # print(company.staffs) # ['danny2', 'danny3']
    print(Company.__init__.__defaults__)

    com1 = Company("company1")
    com1.add("danny4")
    # print(com1.staffs)
    com2 = Company("company2")
    com2.add("danny5")
    print(Company.__init__.__defaults__)
    # 注意：
    print(com2.staffs) #['danny4', 'danny5']
    print(com1.staffs) #['danny4', 'danny5']
    # 原因staffs是可变[]，并且com1和com2都没有传递staff对象,这样导致使用了同一对象
    # print(com1.staffs is com2.staffs)
    # print(Company.__init__.__defaults__)
    # a = 1
    # b = 2
    # c = add(a,b)
    # print(c)
    # print(a,b)

    # list
    a = [1, 2]
    b = [1, 2]
    c = add(a, b)
    # print(c)
    # print(a,b) # [1, 2, 1, 2] [1, 2]

    # tuple
    a = (1, 2)
    b = (1, 2)
    # c = add(a,b)
    # print(c)
    # print(a,b) # (1, 2) (1, 2)
