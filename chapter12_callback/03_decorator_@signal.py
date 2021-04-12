"""
如果有多个函数都需要添加登录验证的功能，每次都需要编写func = decorator(func)这样代码对已有函数进行装饰，这种做法还是比较麻烦。

Python给提供了一个装饰函数更加简单的写法，那就是语法糖，语法糖的书写格式是: @装饰器名字，通过语法糖的方式也可以完成对已有函数的装饰
"""


# 定义装饰器
def decorator(func):
    def inner():
        # 在内部函数里面对已有函数进行装饰
        print('已添加登录认证')
        func()

    return inner


@decorator  # comment = decorator(comment) 装饰器语法糖对该代码进行了封装 左边comment=inner
def comment():
    print('发表评论')


# 调用方式不变
comment()