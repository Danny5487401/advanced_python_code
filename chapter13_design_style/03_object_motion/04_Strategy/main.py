
"""
策略模式
策略模式(Strategy Pattern):它定义了算法家族,分别封装起来,
让他们之间可以相互替换,此模式让算法的变化,不会影响到使用算法的客户.

商场搞活动，可以按正常收费、打折收费、返利收费等支付方式，通过 一个具体的策略类来控制支付方式（也就是不同的算法）
"""


class PaySuper(object):
    # 定义一个支付抽象类

    def pay(self, money):
        pass


class PayNormal(PaySuper):
    # 正常支付子类
    def pay(self, money):
        return money


class PayRebate(PaySuper):
    # 打折支付子类
    def __init__(self, discount):
        self.discount = discount

    def pay(self, money):
        return money * self.discount


class PayReturn(PaySuper):
    # 返利支付子类
    def __init__(self, money_condition, money_return):
        self.money_condition = money_condition
        self.money_return = money_return

    def pay(self, money):
        # 支付满money_conditionc才返利money_return
        if money >= self.money_condition:
            return money - self.money_return
        return money


class Context(object):
    # 定义一个具体的策略类，管理支付方式
    def __init__(self, paysuper):
        self.paysuper = paysuper

    def get_result(self, money):
        return self.paysuper.pay(money)


if __name__ == '__main__':
    money = round(float(input('商品原价：')), 2)
    strategy = dict()
    strategy['1'] = Context(PayNormal())  # 正常支付
    strategy['2'] = Context(PayRebate(0.8))  # 打折支付
    strategy['3'] = Context(PayReturn(100, 10))  # 返利支付
    while True:
        mode = input("选择支付方式：1.原价  2.打8折  3.满100减10 4. 取消支付\r\n")
        if mode not in strategy:
            break
        pay_mode = strategy[mode]
        print("需要支付{}元".format(pay_mode.get_result(money)))


"""
总结：
定义一个上下文管理类，接收一个策略，并根据该策略得出结论，
当需要更改策略时，只需要在实例的时候传入不同的策略就可以，免去了修改类的麻烦
"""
