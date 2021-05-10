
"""
适配器一：
NBA球星中分为前锋，中锋，后卫，它们交流都是英语。
假如中国球星姚明刚开始加入NBA，他肯定不能和队员，教练正确交流，因为他不会英文。
这个时候，我们就需要给姚明请一个翻译人员，既能和姚明交流，又能和教练交流，
翻译人员在这个过程中起的就是一个适配器的作用。
"""
import abc


class Player(metaclass=abc.ABCMeta):
    # 定义一个抽象类
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def attack(self):
        pass

    @abc.abstractmethod
    def defense(self):
        pass


class Forwards(Player):
    # 定义前锋类
    def __init__(self, name):
        Player.__init__(self, name)  # 父类初始化

    def attack(self):
        print("前锋{}进攻".format(self.name))

    def defense(self):
        print("前锋{}防守".format(self.name))


class Center(Player):
    # 定义中锋类
    def __init__(self, name):
        Player.__init__(self, name)  # 父类初始化

    def attack(self):
        print("中锋{}进攻".format(self.name))

    def defense(self):
        print("中锋{}防守".format(self.name))


class Guards(Player):
    # 定义后卫类
    def __init__(self, name):
        Player.__init__(self, name)  # 父类初始化

    def attack(self):
        print("后卫{}进攻".format(self.name))

    def defense(self):
        print("后卫{}防守".format(self.name))


# 当前中锋是姚明，他不认识Attack和Denfense所以需要一个翻译作为适配器，为了适配姚明和英语

class ForeignCenter(object):
    # 定义一个外籍中锋类
    def __init__(self, name):
        self.name = name

    def 攻击(self):
        print("外籍中锋{}在进攻".format(self.name))

    def 防守(self):
        print("外籍中锋{}在防守".format(self.name))


class Transtator(Player):
    # 定义一个翻译人员的类，作为适配器
    def __init__(self, name):
        Player.__init__(self, name)
        self.wjzf = ForeignCenter(name)  # 实例化外籍中锋

    def attack(self):
        self.wjzf.攻击()

    def defense(self):
        self.wjzf.防守()


"""
适配器二：
使用类中的内部字典做适配器
有三个类（一个叫做Computer, 另外两个叫做Synthesizer，Human），
我们现在想做的就是将Computer类和Synthesizer，Human做适配。
假设这三个类都不能改。
用户只知道Computer中的execute()方法，
怎样调用Synthesizer 的play()方法和Human中的speak()方法? 
此时我们就需要考虑做个适配器Adapter。

"""


class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} computer'.format(self.name)

    def execute(self):
        return 'executes a program'


class Synthesizer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} synthesizer'.format(self.name)

    def play(self):
        return 'is playing an electronic song'


class Human:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'the {} human'.format(self.name)

    def speak(self):
        return 'says hello'


class Adapter:
    def __init__(self, obj, adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)  # adapterd_method是一个字典，键是客户调用的方法，值是被调用的方法。

    def __str__(self):
        return str(self.obj)


if __name__ == '__main__':
    print('-------------使用抽象类实现适配器---------------')
    # 前锋实例化
    f_Batir = Forwards("巴蒂尔")
    f_Batir.attack()
    f_Batir.defense()

    # 后卫实例化
    g_Maddie = Guards("麦迪")
    g_Maddie.attack()
    g_Maddie.defense()

    # 中锋实例化
    ym = Transtator("姚明")
    ym.attack()
    ym.defense()

    print("-------------使用类中的内置字典实现适配器---------------")
    objects = [Computer('Dell')]

    synth = Synthesizer('moog')
    objects.append(Adapter(synth, dict(execute=synth.play)))

    human = Human('Danny')
    objects.append(Adapter(human, dict(execute=human.speak)))

    for i in objects:
        print('{} {}'.format(str(i), i.execute()))



"""
总结：
什么时候使用Adapter模式
很多时候，我们并非从0开始编程，特别是当现有的类已经被充分测试过了，Bug很少，
而且已经被用于其他软件之中时，我们更愿意将这些类作为组件重复利用。

Adapter模式会对现有的类进行适配，生成新的类。通过该模式可以很方便地创建我们需要的方法群。
当出现Bug时，由于我们明确知道Bug不在现有的类（Adaptee角色）中，所以只需调查Adapter角色的类即可。

如果没有现成的代码让现有的类适配新的接口（API）时，使用Adapter模式似乎是理所应当的。
在Adapter模式中，并非一定需要现成的代码。只要知道现有类的功能，就可以。

版本升级与兼容性
软件的生命周期总是伴随着版本的升级，而很多时候需要与旧版本兼容。
这个时候可以让新版本扮演Adaptee角色，旧版本扮演Target角色。
接着编写一个Adapter角色的类，让它使用新版本的类来实现旧版本的类中的功能。

功能完全不同的类
当然，当Adaptee角色与Target角色的功能完全不同时，Adapter模式是无法使用的。
就如同我们无法用交流100伏特电压让自来水管出水一样。

"""
