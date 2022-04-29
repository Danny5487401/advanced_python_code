# 函数和类都是对象
def ask(name="danny1"):
    print(name)
    return "danny3"


class Person:
    def __init__(self):
        print("danny2")

    def __str__(self):
        return "call str"


def docorator_func():
    print("装饰器")
    return ask


# 1. 函数赋值给一个变量
myfuc = ask
myfuc("JOY")

# 类赋值给一个变量
myclass = Person
myclass()

# 2. 放在集合当中
obj_list = []
obj_list.append(ask)
obj_list.append(Person)
for item in obj_list:
    print(item())
""" 结果
danny1
danny3 #return结果
danny2
call str # __str__结果
"""

# 3. 返回一个函数给一个变量
my_ask = docorator_func()
my_ask("tom")
