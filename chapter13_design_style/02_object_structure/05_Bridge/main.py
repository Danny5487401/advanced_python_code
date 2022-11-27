
"""
桥接模式
Bridge效果及实现要点：
1．Bridge模式使用“对象间的组合关系”解耦了抽象和实现之间固有的绑定关系，
使得抽象和实现可以沿着各自的维度来变化。

2．所谓抽象和实现沿着各自维度的变化，即“子类化”它们，得到各个子类之后，
便可以任意它们发展，从而获得不同路上的不同汽车。

3．Bridge模式有时候类似于多继承方案，
但是多继承方案往往违背了类的单一职责原则（即一个类只有一个变化的原因），复用性比较差。
Bridge模式是比多继承方案更好的解决方法。

4．Bridge模式的应用一般在“两个非常强的变化维度”，有时候即使有两个变化的维度，
但是某个方向的变化维度并不剧烈——换言之两个变化不会导致纵横交错的结果，并不一定要使用Bridge模式。
"""


class AbstractRoad(object):
    # 路基类
    car = None


class AbstractCar(object):
    # 车辆基类

    def run(self):
        raise NotImplementedError


class Street(AbstractRoad):
    # 市区街道
    def run(self):
        # 执行车辆对象的方法
        self.car.run()
        print("在市区街道上行驶")


class SpeedWay(AbstractRoad):
    # 高速公路
    def run(self):
        # 执行车辆对象的方法
        self.car.run()
        print("在高速公路上行驶")


class Car(AbstractCar):
    # 小汽车
    def run(self):
        # 被其它对象调用执行
        print("小汽车在")


class Bus(AbstractCar):
    # 公共汽车
    def run(self):
        # 被其它对象调用执行
        print("公共汽车在")


if __name__ == '__main__':
    # 小汽车在高速公路上行驶
    road1 = SpeedWay()
    road1.car = Car()
    road1.run()
    print("-----------")
    # 公共汽车在高速公路上行驶
    road2 = SpeedWay()
    road2.car = Bus()
    road2.run()
    print("-----------")
    # 公共汽车在市区上行驶
    road3 = Street()
    road3.car = Bus()
    road3.run()

"""
总结：
Bridge模式是一个非常有用的模式，也非常复杂，它很好的符合了开放-封闭原则和优先使用对象，而不是继承这两个面向对象原则
"""


