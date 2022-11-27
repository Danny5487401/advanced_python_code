
"""
抽象工厂模式
提供一个创建一系列相关或相互依赖对象的接口，而无需指定它们具体的类。
抽象工厂模式与工厂方法模式的最大区别就在于，工厂方法模式针对的是一个产品等级结构；
而抽象工厂模式则需要面对多个产品等级结构。
"""


class AbstractFactory(object):
    # 创建一个抽象工厂
    computer_name = ''  # 电脑名称

    def create_cpu(self):
        # 定义一个创建cpu方法具体实现由子类完成
        pass

    def create_mainboard(self):
        # 定义一个创建主板方法具体实现由子类完成
        pass


class AbstractCpu(object):
    # 定义一个cpu产品抽象类
    series_name = ''
    instructions = ''
    arch = ''


class IntelCpu(AbstractCpu):
    # 定义一个Intel公司的cpu产品类，继承【cpu产品抽象类】
    def __init__(self, series):
        self.series_name = series  # 序列号名称


class AmdCpu(AbstractCpu):
    # 定义一个Amd公司的cpu产品类，继承【cpu产品抽象类】
    def __init__(self, series):
        self.series_name = series  # 序列号名称


class AbstractMainboard(object):
    # 定义一个mainboard(主板)产品抽象类
    series_name = ''


class IntelMainboard(AbstractMainboard):
    # 定义一个Intel公司的mainboard(主板)产品类，继承【mainboard(主板)抽象类】
    def __init__(self, series):
        self.series_name = series  # 序列号名称


class AmdMainboard(AbstractMainboard):
    # 定义一个Amd公司的mainboard(主板)产品类，继承【mainboard(主板)抽象类】
    def __init__(self, series):
        self.series_name = series  # 序列号名称


class IntelFactory(AbstractFactory):
    # 创建一个生产Intel公司产品的工厂，继承抽象工厂类
    computer_name = 'Intel I7-series computer '

    def create_cpu(self):
        # 在工厂里定义一个创建cpu产品方法
        return IntelCpu('I7-6500')

    def create_mainboard(self):
        # 在工厂里定义一个创建mainboard(主板)产品方法
        return IntelCpu('Intel-6000')


class AmdFactory(AbstractFactory):
    # 创建一个生产Amd公司产品的工厂，继承抽象工厂类
    computer_name = 'Amd 4 computer '

    def create_cpu(self):
        # 在工厂里定义一个创建cpu产品方法
        return AmdCpu('amd444')

    def create_mainboard(self):
        # 在工厂里定义一个创建mainboard(主板)产品方法
        return AmdMainboard('AMD-4000')


class ComputerEnginee(object):
    # 定义一个装机工程师
    def make_computer(self, factory_obj):
        self.prepare_hardwares(factory_obj)

    def prepare_hardwares(self, factory_obj):
        # 定义一个硬件装机方法
        self.cpu = factory_obj.create_cpu()
        self.mainboard = factory_obj.create_mainboard()
        info = ''' -----------电脑【{}】信息-----------
            cpu: 【{}】
            mainboaed: 【{}】
        '''.format(factory_obj.computer_name, self.cpu.series_name, self.mainboard.series_name)
        print(info)


if __name__ == '__main__':
    engineer = ComputerEnginee()  # 装机工程师
    intel_factory = IntelFactory()  # Intel工厂
    engineer.make_computer(intel_factory)  # 工程师装Intel的电脑

    amd_factory = AmdFactory()  # Intel工厂
    engineer.make_computer(amd_factory)  # 工程师装Amd的电脑

"""
总结：
抽象工厂和工厂模式的对比区别：
抽象工厂：规定死了，依赖限制，像上面实验，你用intel的机器只能配置intel的CPU不能配置AMD的CPU（由各自的工厂指定自己的产品生产品牌）
工厂模式：不是固定死的，举例：你可使用intel的机器配置AMD的CPU
抽象工厂模式在工厂方法基础上扩展了工厂对多个产品创建的支持，
更适合一些大型系统，
比如系统中有多于一个的产品族，且这些产品族类的产品需实现同样的接口，
像很多软件系统界面中不同主题下不同的按钮、文本框、字体等等。
"""

