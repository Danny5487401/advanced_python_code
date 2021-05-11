
"""
享元模式
享元对象中不会随环境改变而改变的共享部分。比如围棋棋子的颜色。

构造一小片水果树的森林，小到能确保在单个终端页面中阅读整个输出。
然而，无论你构造的森林有多大，内存分配都保持相同。
"""

import random
from enum import Enum

# 定义只有3种树的枚举类型
TreeType = Enum('TreeType', ('apple_tree', 'cherry_tree', 'peach_tree'))


class Tree:
    """
    把Tree类变换成一个元类，元类支持自引用。这意味着cls引用的是Tree类。
    当客户端要创建Tree的一个实例时，会以tree_type参数传递树的种类。
    树的种类用于检查是否创建过相同种类的树。
    如果是，则返回之前创建的对象；
    否则，将这个新的树种添加到池中，并返回相应的新对象，

    """
    pool = dict()  # 创建一个字典缓存。类属性（类的所有实例共享的一个变量）

    def __new__(cls, tree_type):
        obj = cls.pool.get(tree_type, None)  # 从缓存中获取树种类型
        if not obj:
            # 如果获取不到树类型就创建一个新的，并保存到缓存中
            obj = object.__new__(cls)
            cls.pool[tree_type] = obj
            obj.tree_type = tree_type
        return obj

    def render(self, age, x, y):
        """
        用于在屏幕上渲染一棵树。注意，享元不知道的所有可变（外部的）信息都需要客户端代码显示地传递。
        在当前案例中，每棵树都用到一个随机的年龄和一个x,y形式的位置。
        :param age: 树龄
        :param x: x轴
        :param y: y轴
        :return:
        """
        print('render a tree of type {} and age {} at ({}, {})'.format(self.tree_type, age, x, y))


def main():
    rnd = random.Random()
    age_min, age_max = 1, 30  # 树龄单位为年
    min_point, max_point = 0, 100  # 树的坐标0到100
    tree_counter = 0  # 树的数量
    for _ in range(10):
        # 随机生成10棵苹果树
        t1 = Tree(TreeType.apple_tree)
        t1.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1
    print("-----")
    for _ in range(3):
        # 随机生成3棵樱桃树
        t2 = Tree(TreeType.cherry_tree)
        t2.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1
    print("-----")
    for _ in range(5):
        # 随机生成5棵桃子树
        t3 = Tree(TreeType.peach_tree)
        t3.render(rnd.randint(age_min, age_max),
                  rnd.randint(min_point, max_point),
                  rnd.randint(min_point, max_point)
                  )
        tree_counter += 1
    print("-----")
    print('渲染的树数目：{}'.format(tree_counter))
    print('实际上创建的树数目:{}'.format(len(Tree.pool)))
    t4 = Tree(TreeType.cherry_tree)
    t5 = Tree(TreeType.cherry_tree)
    t6 = Tree(TreeType.apple_tree)
    print(id(t4), id(t5), id(t6))


if __name__ == '__main__':
    main()


"""
总结：
在单例的基础上做了改动，也就是当你实例化一个对象，
就判断你实例化的该对象（包含形参）是否存在父类的指定的字典，
存在就把之前实例化对象返回给你（等于没创建新的实例，而是赋值多一个变量而已，指向同一个内存地址），
如果不存在，就创建新的实例化对象返回，并且存放在指定字典
"""
