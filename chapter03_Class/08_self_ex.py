# 自省机制：通过一定的机制查询到对象的内部结构

class Person:
    """introduction"""
    name = "user"


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


if __name__ == "__main__":
    user = Student("厦大")

    # 通过__dict__查询属性以及对应的值， c语言实现

    # 1. 打印实例属性
    print(user.__dict__)  # 打印的是Student属性\
    # dir 只有属性名称，没有对应的值
    print(dir(user))
    # 添加属性
    user.__dict__["school_addr"] = "上海"
    print(user.school_addr)
    print(user.__dict__)  # 打印的是Student属性

    # 2。 打印类的属性
    print(Person.__dict__)  # 类比实例更丰富
    # print(Person.__doc__)
    # print(user.name)


