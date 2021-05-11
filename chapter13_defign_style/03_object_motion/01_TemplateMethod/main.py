# encoding: utf-8
'''
@contact: 1257309054@qq.com
@wechat: 1257309054
@Software: PyCharm
@file: 13、模板方法模式.py
@time: 2020/3/14 19:55
@author:LDC
'''
"""
模板方法模式
在多个算法或框架具有类似或相同的逻辑的时候，可以使用模板方法模式，以实现代码重用。

模板方法模式是一种基于继承的代码复用技术，它是一种类行为型模式。
模板方法模式是结构最简单的行为型设计模式，在其结构中只存在父类与子类之间的继承关系。
通过使用模板方法模式，可以将一些复杂流程的实现步骤封装在一系列基本方法中，
在抽象父类中提供一个称之为模板方法的方法来定义这些基本方法的执行次序，而通过其子类来覆盖某些步骤，
从而使得相同的算法框架可以有不同的执行结果。
模板方法模式提供了一个模板方法来定义算法框架，而某些具体步骤的实现可以在其子类中完成。


"""


class Register(object):
    '''用户登录/注册模板接口'''

    def register(self):
        pass

    def login(self):
        pass

    def auth(self):
        # 模板方法：定义好具体的算法步骤或框架
        self.register()
        self.login()


class RegisterByQQ(Register):
    '''qq注册'''
    # 子类1：按需重新定义模板方法中的算法操作，即重新定义登录和注册方法
    def register(self):
        print("---用qq注册-----")

    def login(self):
        print('----用qq登录-----')


class RegisterByWeiChat(Register):
    '''微信注册'''
    # 子类2：按需重新定义模板方法中的算法操作，即重新定义登录和注册方法
    def register(self):
        print("---用微信注册-----")

    def login(self):
        print('----用微信登录-----')


if __name__ == "__main__":
    register1 = RegisterByQQ()
    register1.auth()
    print("\r")
    register2 = RegisterByWeiChat()
    register2.auth()


"""
总结：
主要角色：
接口：通常是抽象基类，定义模板方法中需要的各项操作。
模板方法：即模板算法，定义好各项操作的执行顺序或算法框架。
真实对象：子类通过重新实现接口中的各项操作，以便让模板方法实现不同的功能。
优缺点：
优点：因为子类的实现是根据基类中的模板而来的，所以可以实现代码重用，
因为有时候我们需要修改的只是模板方法中的部分操作而已。
缺点：此模式的维护有时候可能会很麻烦，因为模板方法是固定的，
一旦模板方法本身有修改的时候，就可能对其他的相关实现造成影响。
"""
