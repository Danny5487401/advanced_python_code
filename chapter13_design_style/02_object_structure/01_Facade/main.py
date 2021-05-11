
"""
外观模式
假设有一组火警报警系统，由三个子元件构成：一个警报器，一个喷水器，一个自动拨打电话的装置。
#当火警发生时，先警报器响起警报，喷水器开始喷水，最后开始拨打火警电话
"""


class AlarmSensor(object):
    # 警报器
    def run(self):
        print('Alarm Ring...')


class WaterSprinkler(object):
    # 喷水器
    def run(self):
        print("Spray Water...")


class EmergencyDialer(object):
    # 拨打火警电话
    def run(self):
        print("Dial 119...")


class EmergencyFacade(object):
    # 定义一个外观类,其中封装对子系统的操作
    def __init__(self):
        self.alarm_sensor = AlarmSensor()
        self.water_sprinkler = WaterSprinkler()
        self.emergency_dialer = EmergencyDialer()

    def run_all(self):
        self.alarm_sensor.run()
        self.water_sprinkler.run()
        self.emergency_dialer.run()


if __name__ == '__main__':
    emergency_facade = EmergencyFacade()
    emergency_facade.run_all()


"""
总结：
根据“单一职责原则”，在软件中将一个系统划分为若干个子系统有利于降低整个系统的复杂性，
一个常见的设计目标是使子系统间的通信和相互依赖关系达到最小，而达到该目标的途径之一就是引入一个外观对象，
它为子系统的访问提供了一个简单而单一的入口。 
外观模式也是“迪米特法则”的体现，通过引入一个新的外观类可以降低原有系统的复杂度，
同时降低客户类与子系统类的耦合度。

外观模式要求一个子系统的外部与其内部的通信通过一个统一的外观对象进行，
外观类将客户端与子系统的内部复杂性分隔开，使得客户端只需要与外观对象打交道，
而不需要与子系统内部的很多对象打交道。 
外观模式的目的在于降低系统的复杂程度。 
外观模式从很大程度上提高了客户端使用的便捷性，使得客户端无须关心子系统的工作细节，通过外观角色即可调用相关功能。

优点：
主要优点在于对客户屏蔽子系统组件，减少了客户处理的对象数目并使得子系统使用起来更加容易，
它实现了子系统与客户之间的松耦合关系，并降低了大型软件系统中的编译依赖性，简化了系统在不同平台之间的移植过程；

缺点：
其缺点在于不能很好地限制客户使用子系统类，而且在不引入抽象外观类的情况下，
增加新的子系统可能需要修改外观类或客户端的源代码，违背了“开闭原则”。

使用情况：
适用情况包括：
要为一个复杂子系统提供一个简单接口；
客户程序与多个子系统之间存在很大的依赖性；
在层次化结构中，需要定义系统中每一层的入口，使得层与层之间不直接产生联系。

"""
