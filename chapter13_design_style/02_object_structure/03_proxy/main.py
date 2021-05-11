
"""
代理模式
应用特性：在通信双方中间需要一些特殊的中间操作时引用，多加一个中间控制层。
结构特性：建立一个中间类，创建一个对象，接收一个对象，然后把两者联通起来
"""


class SenderBase(object):
    # 定义一个发信息的基类
    def send_something(self, something):
        pass


class SendClass(SenderBase):
    # 定义一个发信息的类
    def __init__(self, receiver):
        self.receiver = receiver

    def send_something(self, something):
        print('send {} to {}'.format(something, self.receiver))


class Proxy(SenderBase):
    # 定义一个代理类
    def __init__(self, receiver):
        self.send_obj = SendClass(receiver)

    def send_something(self, something):
        self.send_obj.send_something(something)


class ReceiveClass(object):
    # 定义一个接收类
    def __init__(self, someone):
        self.name = someone

    def __str__(self):
        return self.name


if __name__ == '__main__':
    receiver = ReceiveClass('ldc')
    proxy = Proxy(receiver)
    proxy.send_something('成功使用了代理')
    print(receiver.__class__)
    print(proxy.__class__)


"""
总结：
代理模式为其他对象提供一种代理以控制对这个对象的访问。
代理模式就如同一个"过滤器"，它不实现具体功能，具体功能由被调用的实体来实现，
代理实现的是对调用的控制功能，它能够允许或者拒绝调用实体对被调用实体的访问。
"""
