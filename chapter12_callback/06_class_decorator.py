# 类装饰器
# Note: 函数之所以能够调用，是因为函数内部实现了 __call__ 方法

class MyDecorator(object):
    def __init__(self, func):
        self.__func = func

    # 实现__call__方法，表示对象是一个可调用对象，可以像调用函数一样进行调用
    def __call__(self, *args, **kwargs):
        # 对已有函数进行封装
        print('马上就有下班啦')
        self.__func()


@MyDecorator  # @MyDecorator => show = MyDecorator(show)
def show():
    print('快要下雪啦')


# 执行show，就相当于执行MyDecorator类创建的实例对象，show() => 对象()
show()
