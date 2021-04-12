# 装饰器

"""
业务逻辑：登录之后才能评论
"""
# 定义装饰器
def decorator(func):
    def inner():
        # 在内部函数里面对已有函数进行装饰
        print('已添加登录认证')
        func()

    return inner


def comment():
    print('发表评论')


# 调用装饰器对已有函数进行装饰，左边的comment=inner
comment = decorator(comment)

# 调用方式不变
comment()

