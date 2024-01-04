class User:
    # 类的生成过程
    # 高级框架中经常使用
    def __new__(cls, *args, **kwargs):
        print("in new")
        # new是用来控制对象的生成过程，Init是完善对象的
        # new如果不返回对象，则不调用__init__
        return super().__new__(cls)

    # 对象的生成对象
    def __init__(self, name):
        print("in init")
        self.name = name


if __name__ == "__main__":
    user = User("danny")
    # user = User(name="danny2")
    print(user.name)
