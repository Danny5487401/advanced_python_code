# 生成器函数: 函数里面只要有yield关键字


def gen_func():
    yield 1
    yield 2
    yield 3


# 惰性求值，延迟求值提供了可能
# 斐波拉契求值三种方法
# 打印最终值
def fib(index):
    # 0 1 1 2 3 5 8
    if index <= 2:
        return 1
    else:
        return fib(index-1) + fib(index-2)

# 打印过程
def fib2(index):
    res_list = []
    n,a,b =0,0,1
    while n <index:
        res_list.append(b)
        a,b = b, a+b
        n += 1
    return res_list


# 惰性求值,显示过程
def fib3(index):
    n,a,b = 0,0,1
    while n <index:
        yield b
        a,b = b, a+b
        n += 1

# 对比
def func():
    return 1


if __name__ == "__main__":
    # 生成器对象，python编译字节码的时候就产生
    # gen = gen_func()
    # for value in gen:
    #     print(value)
    # res = func()

    print(fib(5))
    print(fib2(5))
    for data in fib3(5):
        print(data)
    pass

