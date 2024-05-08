class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __str__(self):
        return ",".join(self.employee)

    def __repr__(self):
        # 类的表示
        return "joy"


if __name__ == "__main__":
    # len() 函数性能特别高，c语言内部有一个变量维护
    company = Company(["danny", "tom", "joy"])
    # <__main__.Company object at 0x00000154129D32C8> 完成__str__ 打印danny,tom,joy
    print(company)
    print(repr(company))  # 开发模式调用  jupyter 调用  __repr__
