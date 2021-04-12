#带参数和返回值的装饰器

def decorator(func):
    def inner(num1, num2):
        print('正在努力执行加法计算')
        num = func(num1, num2)
        return num

    return inner


@decorator
def add_num(num1, num2):
    result = num1 + num2
    return result


result = add_num(1, 2)
print(f'结果为：{result}')