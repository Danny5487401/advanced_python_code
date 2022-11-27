
"""
迭代器模式
迭代器模式(Iterator Pattern):提供方法顺序访问一个聚合对象中各元素，而又不暴露该对象的内部表示.
"""


class Iterator(object):
    # 迭代器抽象类
    def first(self):
        # 第一个
        pass

    def next(self):
        # 下一个
        pass

    def is_done(self):
        # 是否完成
        pass

    def current_item(self):
        # 当前项目
        pass


class Aggregate(object):
    # 聚集抽象类
    def create_iterator(self):
        # 创建迭代器
        pass


class ConcreteIterator(Iterator):
    # 具体迭代器类，顺序
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = 0

    def first(self):
        return self.aggregate[0]

    def next(self):
        ret = None
        self.curr += 1
        if self.curr < len(self.aggregate):
            ret = self.aggregate[self.curr]
        return ret

    def is_done(self):
        return True if self.curr + 1 >= len(self.aggregate) else False

    def current_item(self):
        return self.aggregate[self.curr]


class ConcreteAggregate(Aggregate):
    # 具体聚集类

    def __init__(self):
        self.i_list = []

    def create_iterator(self):
        return ConcreteIterator(self)


class ConcreteIteratorDesc(Iterator):
    # 具体迭代器类，倒序
    def __init__(self, aggregate):
        self.aggregate = aggregate
        self.curr = len(aggregate) - 1

    def first(self):
        return self.aggregate[-1]

    def next(self):
        ret = None
        self.curr -= 1
        if self.curr >= 0:
            ret = self.aggregate[self.curr]
        return ret

    def is_done(self):
        return True if self.curr - 1 < 0 else False

    def current_item(self):
        return self.aggregate[self.curr]


if __name__ == '__main__':
    ca = ConcreteAggregate()  # 创建具体聚集
    ca.i_list.append("房子")
    ca.i_list.append("沙发")
    ca.i_list.append("衣柜")
    ca.i_list.append("床")

    itor = ConcreteIterator(ca.i_list)  # 创建一个迭代器
    print(itor.first())
    while not itor.is_done():
        print(itor.next())

    print('*********倒序**********')
    itor_desc = ConcreteIteratorDesc(ca.i_list)  # 创建一个迭代器
    print(itor_desc.first())
    while not itor_desc.is_done():
        print(itor_desc.next())


"""
总结：
当需要对聚集对象有多种方式遍历时，可以考虑使用迭代器模式
迭代器模式分离了集合的遍历行为，抽象出一个迭代器类来负责，这样既可以做到不暴露集合内部结构，
又可以让外部代码透明的访问集合内部的数据

优点： 1、它支持以不同的方式遍历一个聚合对象。 
2、迭代器简化了聚合类。 
3、在同一个聚合上可以有多个遍历。 
4、在迭代器模式中，增加新的聚合类和迭代器类都很方便，无须修改原有代码。

缺点：由于迭代器模式将存储数据和遍历数据的职责分离，增加新的聚合类需要对应增加新的迭代器类，
类的个数成对增加，这在一定程度上增加了系统的复杂性。
"""
