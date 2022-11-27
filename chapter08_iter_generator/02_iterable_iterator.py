from collections.abc import Iterator


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        # next 让外部去处理
        return MyIterator(self.employee)
    #     return 1 # TypeError: iter() returned non-iterator of type 'int'

    #
    # def __getitem__(self, item):
    #     # item是索引
    #     return self.employee[item]


class MyIterator(Iterator):
    def __init__(self, employee_list):
        self.iter_list = employee_list
        # 这里维护所以
        self.index = 0

    # def __iter__(self):
    #     return self
    def __next__(self):
        # 不支持切片
        # 真正返回迭代值的逻辑
        try:
            word = self.iter_list[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == "__main__":
    company = Company(["danny", "tom", "joy"])
    my_itor = iter(company)
    while True:
        try:
            print(next(my_itor))
        except StopIteration:
            break

    # 调用iter(company)
    for item in company:
        print(item)
