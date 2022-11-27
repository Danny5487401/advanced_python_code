# 装饰器应用

# 装饰器实现已有函数执行时间的统计

import time


def decorator(func):
    def inner():
        # 获取时间距离1970-1-1 0:0:1的时间差
        begin = time.time()
        func()
        end = time.time()
        result = end - begin
        print(f'函数执行完成耗时：{result}')

    return inner


@decorator
def work():
    for i in range(10000):
        print(i)


work()
