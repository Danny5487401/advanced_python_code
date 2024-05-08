import pickle


class Person(object):
    def __init__(self, name, age, birthday):
        self.name = name
        self.age = age
        self.birthday = birthday

    def __getstate__(self):
        # 执行 pick.dumps 时 忽略 age 属性
        return {"name": self.name, "birthday": self.birthday}

    def __setstate__(self, state):
        # 执行 pick.loads 时 忽略 age 属性
        self.name = state["name"]
        self.birthday = state["birthday"]


if __name__ == "__main__":
    person = Person("李四", 20, (2017, 2, 23))
    pickled_person = pickle.dumps(person)  # 自动执行 __getstate__ 方法

    p = pickle.loads(pickled_person)  # 自动执行 __setstate__ 方法
    print(p.name, p.birthday)  # 李四 (2017, 2, 23)
    # 由于执行 pick.loads 时 忽略 age 属性，所以下面执行回报错
    print(p.age)  # AttributeError: 'Person' object has no attribute 'age'
