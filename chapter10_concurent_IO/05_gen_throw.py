def gen_func():
    # 这行代码两个作用：产生值，调用方传入值

    # yield "http://www.baidu.com"  # Exception: download error
    try:
        yield "http://www.baidu.com"
    except Exception as e:
        pass
    yield 2
    yield 3
    return "danny"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    print(gen.throw(Exception,"download error"))  # 2
    print(next(gen)) # 3