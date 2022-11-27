#     装饰器装饰同一个类里的函数
#  背景： 想要通过装饰器修改类里的self属性值。
class Buy(object):
    def __init__(self):
        self.reset = True  # 定义一个类属性，稍后在装饰器里更改
        self.func = True

    # 在类里定义一个装饰器
    def clothes(func):  # func接收body
        def ware(self, *args, **kwargs):  # self,接收body里的self,也就是类实例
            print('This is a decrator!')
            if self.reset == True:  # 判断类属性
                print('Reset is Ture, change Func..')
                self.func = False  # 修改类属性
            else:
                print('reset is False.')

            return func(self, *args, **kwargs)

        return ware

    @clothes
    def body(self):
        print('The body feels could!')


if __name__ == "__main__":
    b = Buy()  # 实例化类
    b.body()  # 运行body
    print(b.func)  # 查看更改后的self.func值，是False，说明修改完成
