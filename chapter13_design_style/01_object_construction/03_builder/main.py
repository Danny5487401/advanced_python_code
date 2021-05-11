
"""
创建者模式
相关模式：思路和模板方法模式很像，模板方法是封装算法流程，对某些细节，提供接口由子类修改，
创建者模式更为高层一点，将所有细节都交由子类实现。
创建者模式：将一个复杂对象的构建与他的表示分离，使得同样的构建过程可以创建不同的表示。
基本思想
某类产品的构建由很多复杂组件组成；
这些组件中的某些细节不同，构建出的产品表象会略有不同；
通过一个指挥者按照产品的创建步骤来一步步执行产品的创建；
当需要创建不同的产品时，只需要派生一个具体的创建者，重写相应的组件构建方法即可。
"""


# 定义一个创建者基类
class PersonBuilder(object):

    def build_head(self):
        pass

    def build_body(self):
        pass

    def build_arm(self):
        pass

    def build_leg(self):
        pass


# 胖子
class PersonFatBuilder(PersonBuilder):
    type = '胖子'

    def build_head(self):
        info = "构建{}的大...头".format(self.type)
        print(info)

    def build_body(self):
        info = "构建{}的身体".format(self.type)
        print(info)

    def build_arm(self):
        info = "构建{}的手".format(self.type)
        print(info)

    def build_leg(self):
        info = "构建{}的脚".format(self.type)
        print(info)


# 瘦子
class PersonThinBuilder(PersonBuilder):
    type = '瘦子'

    def build_head(self):
        info = "构建{}的头".format(self.type)
        print(info)

    def build_body(self):
        # 注意与别的产品细节不同
        info = "构建{}的瘦小身体".format(self.type)
        print(info)

    def build_arm(self):
        info = "构建{}的手".format(self.type)
        print(info)

    def build_leg(self):
        info = "构建{}的脚".format(self.type)
        print(info)


# 指挥者
class PersonDirector(object):
    pd = None

    def __init__(self, pd):
        self.pd = pd

    def create_person(self):
        # 指挥者按照产品的创建步骤来一步步执行产品的创建
        self.pd.build_head()
        self.pd.build_body()
        self.pd.build_arm()
        self.pd.build_leg()


class ClientUI(object):
    pb_fat = PersonFatBuilder()  # 创建胖子组件
    pd = PersonDirector(pb_fat)  # 创建指挥者
    pd.create_person()  # 指挥者组建胖子这一个产品
    print("-----")
    pb_thin = PersonThinBuilder()  # 创建瘦子组件
    pd.pd = pb_thin  # 指挥者要创建的产品改为瘦子
    pd.create_person()  # 创建产品


if __name__ == '__main__':
    ClientUI()

