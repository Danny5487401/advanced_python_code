"""
调停者模式/中介者模式
将类与类之间的复杂相互调用，由一个类来协调。解耦
以生产者和消费者之间的销售作为一个中介者，用对象来表示生产和购买及流通这个过程
"""


class Mediator(object):
    # 定义一个抽象中介者类
    def __init__(self):
        self.name = '中介者'
        self.consumer = None
        self.producer = None

    def sale(self):
        # 销售
        self.consumer.shopping(self.producer.name)

    def shopping(self):
        # 购买
        self.producer.sale(self.consumer.name)

    def profit(self):
        # 利润
        print('中介: 我净赚：{}'.format(self.consumer.price - self.producer.price))

    def complete(self):
        # 交易
        self.shopping()  # 先进货后购买
        self.sale()
        self.profit()


class Consumer(object):
    # 消费者
    def __init__(self, product, price):
        self.name = "消费者"
        self.product = product
        self.price = price

    def shopping(self, name):
        # 买东西
        print("{}：购买了{}的{},价格{}".format(self.name, name, self.product, self.price))


class Producer(object):
    # 生产者
    def __init__(self, product, price):
        self.name = "生产者"
        self.product = product
        self.price = price

    def sale(self, name):
        # 卖东西
        print("{}:向{}销售{},价格{}".format(self.name, name, self.product, self.price))


if __name__ == '__main__':
    mediator = Mediator()  # 创建一个中介者
    consumer = Consumer('手机', 3000)  # 创建一个消费者
    producer = Producer('手机', 2500)  # 创建一个生产者
    mediator.consumer = consumer
    mediator.producer = producer
    mediator.complete()

"""
总结：

调停者模式的优点
调停者对象的存在保证了对象结构上的稳定，
也就是说，系统的结构不会因 为新对象的引入造成大量的修改工作。
　　●松散耦合
　　调停者模式通过把多个组件对象之间的交互封装到调停者对象里面，从而使得组件对象之间松散耦合，
    基本上可以做到互补依赖。这样一来，组件对象就可以独立地变化和复用，而不再像以前那样“牵一处而动全身”了。
　　●集中控制交互
　　多个组件对象的交互，被封装在调停者对象里面集中管理，使得这些交互行为发生变化的时候，
    只需要修改调停者对象就可以了，当然如果是已经做好的系统，那么就扩展调停者对象，而各个组件类不需要做修改。
　　●多对多变成一对多
　　没有使用调停者模式的时候，组件对象之间的关系通常是多对多的，引入调停者对象以后，
    调停者对象和组件对象的关系通常变成双向的一对多，这会让对象的关系更容易理解和实现。
调停者模式的缺点
　　调停者模式的一个潜在缺点是，过度集中化。如果组件对象的交互非常多，而且比较复杂，当这些复杂性全部集中到调停者的时候，
    会导致调停者对象变得十分复杂，而且难于管理和维护。
"""

