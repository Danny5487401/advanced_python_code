# 定义一个类装饰器，装饰函数，默认调用__call__方法
class Decrator(object):
    def __init__(self, func):  # 传送的是test方法
        self.func = func

    def __call__(self, *args, **kwargs):  # 接受任意参数
        print('函数调用CALL')
        return self.func(*args, **kwargs)  # 适应test的任意参数


@Decrator  # 如果带参数，init中的func是此参数。
def test(hh):
    print('this is the test of the function !', hh)


test('hh')
