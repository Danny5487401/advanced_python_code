# 先__init__ 再__enter__


class C:
    def __new__(cls, *args, **kwargs):
        print("__new__()方法被调用了")
        print("这个是*agrs", *args)
        print("这个是kwagrs", **kwargs)

        # cls表示这个类，剩余所有的参数传给__init__()方法，
        # 若不返回，则__init__()不会被调用
        return object.__new__(cls)

    def __init__(self):
        print("init")

    def __enter__(self):
        print("enter")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("exit")

    def __del__(self):
        print("del")


# if __name__ == '__main__':
#     a = C() #init
#     print("st")
#     with a:
#         print("hi")
#     with a:
#         print("hi")
#     print("ed")

if __name__ == "__main__":
    print("---start---")
    with C():
        print("hi")
    with C():
        print("hi")
    print("---end---")
