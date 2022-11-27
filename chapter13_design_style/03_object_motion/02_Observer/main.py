"""
观察者模式
观察者（Observer）模式又名发布-订阅（Publish/Subscribe）模式
当我们希望一个对象的状态发生变化，那么依赖于它的所有对象都能相应变化(获得通知),
那么就可以用到Observer模式， 其中的这些依赖对象就是观察者的对象，
那个要发生变化的对象就是所谓’观察者’

"""


class ObserverBase(object):
    # 观察者基类，放哨者
    def __init__(self):
        self._observerd_list = []  # 被通知对象

    def attach(self, observe_subject):
        """
        添加要观察的对象
        """
        if observe_subject not in self._observerd_list:
            self._observerd_list.append(observe_subject)
            print("【{}】已经将【{}】加入观察队列...".format(self.name, observe_subject))

    def detach(self, observe_subject):
        """
        解除观察关系
        :param observe_subject:
        :return:
        """
        try:
            self._observerd_list.remove(observe_subject)
            print("不再观察【{}】".format(observe_subject))
        except ValueError:
            pass

    def notify(self):
        """
        通知所有被观察者
        :return:
        """
        for observer in self._observerd_list:
            observer.update(self)


class Observer(ObserverBase):
    # 观察者类
    def __init__(self, name):
        super(Observer, self).__init__()
        self.name = name
        self._msg = ''

    @property  # 外部执行o.msg 去掉括号
    def msg(self):
        # 当前状况
        return self._msg

    @msg.setter  # 设置属性(一个方法变成一个静态的属性)
    def msg(self, content):
        self._msg = content
        self.notify()


class ATeamViews(object):
    """
    A军观察者
    """

    def update(self, observer_subject):
        print("A军：收到【{}】消息【{}】".format(observer_subject.name, observer_subject.msg))


class BTeamViews(object):
    """
    B军观察者
    """

    def update(self, observer_subject):
        print("B军：收到【{}】消息【{}】".format(observer_subject.name, observer_subject.msg))


if __name__ == '__main__':
    # 初始化A军放哨者
    observer_A = Observer("A军放哨者")
    # 初始化B军放哨者
    observer_B = Observer("B军放哨者")

    A_jun = ATeamViews()
    B_jun = BTeamViews()

    observer_A.attach(A_jun)
    observer_A.attach(B_jun)
    observer_B.attach(B_jun)

    observer_A.msg = "\033[32;1mB军来了...\033[0m"  # 字体样式

    observer_B.msg = "\033[31;1m前方发现A军，请紧急撤离，不要告诉A军\033[0m"

"""
总结：
通过代码了解其实就是发布订阅模式
优点：
独立封装，互不影响：观察者和被观察者都是独自封装好的，观察者之间并不会相互影响
热插拔：在软件运行中，可以动态添加和删除观察者
"""
