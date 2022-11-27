# 生成器是有状态，暂停,挂起，创建
import inspect
def gen_func():
    yield 1
    return "danny"

def gen_func1():
    # 两层含义-》协程
    value = yield 1
    return "danny"

def gen_func2():
    # 两层含义-》协程
    # 遇到费时间的IO就要yield出去，暂停函数
    value = yield from 1
    return "danny"

# 1.希望同步的方式编写异步代码
# 2.可以暂停，可以启动

if __name__ == "__main__":
    gen = gen_func()
    print(inspect.getgeneratorstate(gen)) #GEN_CREATED

    next(gen)
    print(inspect.getgeneratorstate(gen)) # GEN_SUSPENDED

    try:
        next(gen)
    except StopIteration as e:
        pass
    print(inspect.getgeneratorstate(gen)) # GEN_CLOSED