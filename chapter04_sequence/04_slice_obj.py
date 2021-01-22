import numbers


class Group:

    # 支持切片操作

    def __init__(self,group_name,company_name,staffs):
        self.group_name = group_name
        self.company_name = company_name
        self.staffs = staffs

    def __iter__(self):
        return iter(self.staffs)

    def __reversed__(self):
        return self.staffs.reverse()

    # 切片操作
    def __getitem__(self, item):
        # print(item)  # slice(0, 1, None)  返回slice对象
        # return self.staffs[item]
        # 希望切片后还是group,  像queryset一样
        cls = type(self) # <class '__main__.Group'>
        if isinstance(item,slice):
            return cls(group_name=self.group_name,company_name=self.company_name,staffs = self.staffs[item])
        elif isinstance(item,numbers.Integral):
            return cls(group_name=self.group_name, company_name=self.company_name, staffs=[self.staffs[item]])
        print(cls)

    def __len__(self):
        return len(self.staffs)

    # if in 函数
    def __contains__(self, item):
        if item in self.staffs:
            return True
        else:
            return False


staffs = ["danny","Hoy", "June"]
group = Group("厦大","京东",staffs)
sub_group1 = group[0:2]
sub_group2 = group[0]
pass
print(len(group))
if "danny" in group:
    print("yes")
# reversed(group)
for user in group:
    print(user)

