# 鸭子类型： 当你看到一只鸟走起来和游泳起来像鸭子，他就像鸭子

class Cat:
    def say(self):
        print("i am a cat")


class Dog:
    def say(self):
        print("i am a dog")


class Duck:
    def say(self):
        print("i am a duck")


class Company:
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        # item是索引  变成可迭代对象
        return self.employee[item]


# 魔法方法不是Object的，是自己添加的
company = Company(["danny", "tom", "joy"])

# 1. 都实现了say()方法
# animal = Cat
# animal().say()
# 同一方法被调用 ，多态
animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()


# 2. 都是可迭代对象：分别放入列表，集合，迭代对象
a = ["danny1", "danny2"]
b = ["danny5", "danny6"]
name_tuple = ["danny7", "danny8"]

name_set = set()
name_set.add("danny3")
name_set.add("danny4")

a.extend(b)
a.extend(name_tuple)
a.extend(name_set)
a.extend(company)
print(a)
