

"""
组合模式
Composite模式采用 树性结构 来实现普遍存在的对象容器，
从而将一对多的关系转化为一对一的关系，使得客户代码可以一致地(复用)处理对象和对象容器，
无需关心处理的是单个的对象，还是组合的对象容器。
客户代码与纯粹的抽象接口——而非对象容器的内部实现结构——发生依赖，
从而更能”应对变化“。
Composite模式在具体实现中，可以让父对象中的子对象反向追溯；
如果父对象有频繁的遍历需求，可使用缓存技术来改善效率。

会员卡消费，首先

1.我们的部件有，总店，分店，加盟店！
2.我们的部件共有的行为是：刷会员卡
3.部件之间的层次关系，也就是店面的层次关系是，总店下有分店、分店下可以拥有加盟店。
有了我们这几个必要条件后，要求就是目前店面搞活动当我在总店刷卡后，就可以累积相当于在所有下级店面刷卡的积分总额

"""


class Sotre(object):
    # 定义一个组织类，店面基类

    # 添加店面
    def add(self, store):
        pass

    # 删除店面
    def remove(self, store):
        pass

    # 显示店面
    def display(self, depth):
        pass

    # 刷消费卡
    def pay_by_card(self):
        pass


class BranceStore(Sotre):
    # 定义分店类（总店是第一个店，与其它分店功能类似）
    def __init__(self, name):
        self.name = name  # 店名
        self.my_store_list = []  # 开的分店

    def add(self, store):
        # 添加店面
        self.my_store_list.append(store)

    def remove(self, store):
        # 删除店面
        self.my_store_list.remove(store)

    def display(self, depth):
        # 显示店面
        # print(self.name, depth, self.my_store_list)
        print('{}-{}'.format(' ' * depth, self.name))
        for store in self.my_store_list:
            store.display(depth + 2)

    def pay_by_card(self):
        print("店面[%s]的积分已累加进该会员卡" % self.name)
        for s in self.my_store_list:
            s.pay_by_card()


class JoinStore(Sotre):
    # 定义加盟店

    def __init__(self, name):
        self.name = name

    def pay_by_card(self):
        print("店面[%s]的积分已累加进该会员卡" % self.name)

    def add(self, store):
        print("无添加子店权限")

    def remove(self, store):
        print("无删除子店权限")

    def display(self, depth):
        print('{}-{}'.format(' ' * depth, self.name))


if __name__ == '__main__':
    store = BranceStore('广州总店')
    brance = BranceStore('天河分店')
    store.add(brance)  # 总店开分店
    tx_join_brance = JoinStore('棠下加盟店')
    yg_join_brance = JoinStore('元岗加盟店')
    brance.add(tx_join_brance)  # 分店开加盟店
    brance.add(yg_join_brance)  # 分店开加盟店

    store.display(1)
    store.pay_by_card()

"""
总结：
这样在累积所有子店面积分的时候，就不需要去关心子店面的个数了，也不用关心是否是叶子节点还是组合节点了，
也就是说不管是总店刷卡，还是加盟店刷卡，都可以正确有效的计算出活动积分。
应用场景：
在需要体现部分与整体层次的结构时
希望用户忽略组合对象与单个对象的不同，统一的使用组合结构中的所有对象时
"""

