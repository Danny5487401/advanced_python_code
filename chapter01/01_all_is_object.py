# 函数和类都是对象


def ask(name="danny1"):
    print(name)
    return "danny3"

class Person:
    def __init__(self):
        print("danny2")


def docorator_func():
    print("装饰器")
    return ask
# 1. 函数赋值给一个变量
# myfuc = ask
# myfuc("JOY")

# myclass = Person
# # 实例化
# myclass()

# 2. 放在集合当中
# obj_list =[]
# obj_list.append(ask)
# obj_list.append(Person)
# for item in obj_list:
#     print(item())

# 返回一个函数
my_ask = docorator_func()
my_ask("tom")
