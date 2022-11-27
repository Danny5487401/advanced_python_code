# 不定长参数 使用


def test1(a, b, *args, **kwargs):
    print("a:", a, "\n")
    print("b:", b, "\n")
    print("args:", args, "\n")
    print("kwargs:", kwargs, "\n")
    # 方式一
    test2(a, b, args, kwargs)  # 相当于test2(11, 22, (33, 44, 55, 66), {"name":"laowang", "age":18})
    # 方式二
    # test2(a, b, *args, kwargs)  # 相当于test2(11, 22, 33, 44, 55, 66, {"name":"laowang", "age":18})
    # 方式三
    # test2(a, b, *args, **kwargs)  # 相当于test2(11, 22, 33, 44, 55, 66, name="laowang", age=18)

    test3(a, b, args, name=kwargs.get("name"), age=kwargs.get("age"))


def test2(a, b, *args, **kwargs):
    print("---test2---")
    print("a:", a, "\n")
    print("b:", b, "\n")
    print("args:", args, "\n")
    print("kwargs:", kwargs, "\n")


def test3(a, b, args, name, age):
    print("---test3---")
    print("a:", a, "\n")
    print("b:", b, "\n")
    print("args:", args, "\n")
    print("name:", name, "\n")
    print("age:", age, "\n")


test1(11, 22, 33, 44, 55, 66, name="laowang", age=18)
