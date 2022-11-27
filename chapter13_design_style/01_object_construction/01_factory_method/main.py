
"""
工厂模式
工厂模式是一个在软件开发中用来创建对象的设计模式。
工厂模式包涵一个超类。这个超类提供一个抽象化的接口来创建一个特定类型的对象，而不是决定哪个对象可以被创建。
为了实现此方法，需要创建一个工厂类创建并返回。
当程序运行输入一个“类型”的时候，需要创建于此相应的对象。
这就用到了工厂模式。在如此情形中，实现代码基于工厂模式，
可以达到可扩展，可维护的代码。
当增加一个新的类型，不在需要修改已存在的类，只增加能够产生新类型的子类。
举例：
多种品牌的汽车4S店
当买车时，有很多种品牌可以选择，比如北京现代、别克、凯迪拉克、特斯拉等，
那么此时该怎样进行设计呢？
这时就可以用到工厂类
"""


class CarStore(object):
    # 定义一个4S店基类

    def create_car(self, type_name):
        """
        type_name 汽车名称
        """
        # 定义一个创建汽车的方法，但没有实现具体功能，而具体功能需要在子类中实现
        pass

    def order(self, type_name):
        # 让工厂根据类型，生产一辆汽车
        self.car = self.create_car(type_name)
        self.car.move()
        self.car.stop()


# 定义车类型
class YilanteCar(object):
    # 定义伊兰特车类
    def move(self):
        # 定义车的方法，移动
        print("---伊兰特车在移动---")

    def stop(self):
        # 定义车的方法，停车
        print("---伊兰特停车---")


# 定义车类型
class BiekeCar(object):
    # 定义别克车类
    def move(self):
        # 定义车的方法，移动
        print("---别克车在移动---")

    def stop(self):
        # 定义车的方法，停车
        print("---别克停车---")


# 定义一个生产汽车的工厂，让其根据具体的订单生产车
class CarFactory(object):
    # 创建汽车
    def create_car(self, type_name):
        self.type_name = type_name
        if self.type_name == '伊兰特':
            self.car = YilanteCar()
        elif self.type_name == '别克':
            self.car = BiekeCar()
        else:
            self.car = None
        return self.car


# 定义一个广州现代4S店类
class XiandaiCarStore(CarStore):

    def create_car(self, type_name):
        # 在具体子类中实现父类的创建汽车的方法
        # 子类调用工厂创建汽车
        self.car_factory = CarFactory()
        return self.car_factory.create_car(type_name)


if __name__ == '__main__':
    yilante = XiandaiCarStore()
    yilante.order("伊兰特")

"""
总结：其实这个方法，就是无限的罗列需要考虑的情况并给出对应的处理。
缺点：如果我们要新增一个“产品”，
      例如宝马BMW的汽车，除了新增一个iBMW类外还要修改CarFactory内的create_car方法。
      这样就违背了软件设计中的开闭原则[1]，即在扩展新的类时，尽量不要修改原有代码。
改进：1、使用多个工厂，增加一个产品，同时增加一个工厂
      2、使用抽象工厂模式
"""


