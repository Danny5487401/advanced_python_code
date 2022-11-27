"""
访问者模式
安排不同年份的财务报表给不同的角色分析，这就是访问者模式的魅力；
访问者模式的核心是在保持原有数据结构的基础上，实现多种数据的处理方法，
该方法的角色就是访问者。
"""


class Finance(object):
    # 定义一个财务类
    def __init__(self):
        self.salesvolume = None  # 销售额
        self.cost = None  # 成本
        self.history_salesvolume = None  # 历史销售额
        self.history_cost = None  # 历史成本

    def set_salesvolume(self, value):
        self.salesvolume = value

    def set_cost(self, value):
        self.cost = value

    def set_history_salesvolume(self, value):
        self.history_salesvolume = value

    def set_history_cost(self, value):
        self.history_cost = value

    def accept(self):
        pass


class FinanceYear(Finance):
    def __init__(self, year):
        Finance.__init__(self)
        self.analyst = []
        self.year = year

    def add_analyst(self, worker):
        # 增加分析师来分析数据
        self.analyst.append(worker)

    def accept(self):
        # 分析师分析数据
        for a in self.analyst:
            a.visit(self)


class Accounting(object):
    # 会计
    def __init__(self):
        self.name = '会计'
        self.duty = '计算报表'

    def visit(self, year_data):
        print('我现在分析的是{}年的数据'.format(year_data.year))
        print('我的身份是:{}，职责：{}'.format(self.name, self.duty))
        print('本年度纯利润:{}'.format(year_data.salesvolume - year_data.cost))
        print('---------------------------------------')


class Audit:
    # 财务总监
    def __init__(self):
        self.name = '财务总监'
        self.duty = '分析业绩'

    def visit(self, year_data):  # 要把具体哪一年的数据传给分析师，让分析师去分析
        print('我现在分析的是{}年的数据'.format(year_data.year))
        print('我的身份是:{}，职责：{}'.format(self.name, self.duty))
        if year_data.salesvolume - year_data.cost > year_data.history_salesvolume - year_data.history_cost:
            msg = '较同期上涨'
        else:
            msg = '较同期下跌'
        print('本年度公司业绩:{}'.format(msg))
        print('---------------------------------')


class Advisor:
    # 战略顾问
    def __init__(self):
        self.name = '战略顾问'
        self.duty = '制定明年策略'

    def visit(self, year_data):
        print('我现在分析的是{}年的数据'.format(year_data.year))
        print('我的身份是:{}，职责：{}'.format(self.name, self.duty))
        if year_data.salesvolume > year_data.history_salesvolume:
            msg = '行业上涨，扩大规模'
        else:
            msg = '行业下跌，减少规模'
        print('本年度公司业绩:{}'.format(msg))
        print('------------------------------')


class AnalyseData(object):
    # 执行分析
    def __init__(self):
        self.datalist = []  # 需要处理的数据列表

    def add_data(self, year_data):
        self.datalist.append(year_data)

    def remove_data(self, year_data):
        self.datalist.remove(year_data)

    def visit(self):
        for d in self.datalist:
            d.accept()


if __name__ == '__main__':
    w = AnalyseData()  # 计划安排财务，总监，顾问对2020年数据进行分析
    finance_2020 = FinanceYear(2020)  # 2020年财务数据
    finance_2020.set_salesvolume(200)
    finance_2020.set_cost(90)
    finance_2020.set_history_salesvolume(190)
    finance_2020.set_history_cost(80)

    accounting = Accounting()
    audit = Audit()
    advisor = Advisor()

    finance_2020.add_analyst(accounting)  # 会计参与2020年的数据分析，然后执行了自己的visit方法
    finance_2020.add_analyst(audit)
    finance_2020.add_analyst(advisor)
    # finance_2020.accept() # 也可以直接这样调用
    w.add_data(finance_2020)
    w.visit()
"""
总结：
访问者模式优点
1)使得数据结构和作用于结构上的操作解耦，使得操作集合可以独立变化。
2)添加新的操作或者说访问者会非常容易。
3)将对各个元素的一组操作集中在一个访问者类当中。
4)使得类层次结构不改变的情况下，可以针对各个层次做出不同的操作，而不影响类层次结构的完整性。
5)可以跨越类层次结构，访问不同层次的元素类，做出相应的操作。
6)如果操作的逻辑改变，我们只需要改变访问者的实现就够了，而不用去修改其他所有的类。
7)添加新的访问者到系统变得容易。只需要改变一下访问者接口以及其实现。已经存在的访问者不会被干扰影响。



访问者模式缺点
1)实现起来比较复杂，会增加系统的复杂性。
2)visit()方法的返回值的类型在设计系统式就需要明确。
不然，就需要修改访问者的接口以及所有接口实现。
另外如果访问者接口的实现太多，系统的扩展性就会下降。

"""

