def gen_func():
    # 这行代码两个作用：产生值，调用方传入值
    try:
        yield "http://www.baidu.com"
    except GeneratorExit:

        # GeneratorExit  继承BaseException,没有继承Exception
        pass
        # raise StopIteration
    # yield 2
    # yield 3
    return "danny"


if __name__ == "__main__":
    gen = gen_func()
    print(next(gen))
    gen.close()
    # StopIteration,一下执行不了next(
    # next(gen)
