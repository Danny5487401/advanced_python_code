from datetime import date, datetime


class User:
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        # 不像对外暴露，只是规范而已
        self._age = 0

    # 获取年龄 方法一
    # def get_age(self):
    #       return datetime.now().year - self.birthday.year

    # 方法二 获取年龄
    # 属性描述符
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == "__main__":
    user = User("danny", date(year=2000, month=1, day=11))
    # print("in {}file" .format(__file__))
    # 调用方法获取年龄
    # print(user.get_age())
    # 喜欢用obj.age获取 属性
    user.age = 31
    print(user._age)  # 31
    print(user.age)
