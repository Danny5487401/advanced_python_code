# 定义一个类装饰器，装饰类中的函数，默认调用__get__方法
class Decrator(object):
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        '''
        instance:代表实例，sum中的self
        owner：代表类本身，Test类

        '''
        print('%s调用的是get函数' %owner)
        return self.func(instance)  # instance就是Test类的self


class Test(object):
    def __init__(self):
        self.result = 0

    @Decrator
    def sum(self):
        print('There is the Func in the Class !')


if __name__ == "__main__":
    t = Test()
    print(t.sum)  # 众所周知，属性是不加括号的,sum真的变成了属性
