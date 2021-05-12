
"""
备忘录模式
备忘录模式，在不破坏封装性的前提下，捕获一个对象的内部状态，并在该对象之外保存这个状态，
这样以后就可将该对象恢复到原先保存的状态；
在备忘录模式中，如果要保存的状态多，可以创造一个备忘录管理者角色来管理备忘录。
比如保存游戏进度的功能
"""
import random


class Memento(object):
    # 定义一个备忘录类
    vitality = 0  # s生命值
    attack = 0  # 攻击
    defense = 0  # 防御

    def save_state(self, vitality, attack, defense):
        # 保存状态
        self.vitality = vitality
        self.attack = attack
        self.defense = defense
        return self


class GameCharacter(object):
    # 定义一个游戏角色抽象类
    vitality = 0  # s生命值
    attack = 0  # 攻击
    defense = 0  # 防御

    def display_state(self):
        # 显示状态
        print("\033[31;1m当前状态\033[0m")
        print("生命值：{}".format(self.vitality))
        print("攻击值：{}".format(self.attack))
        print("防守值：{}".format(self.defense))

    def init_state(self, vitality, attack, defense):
        # 初始化状态
        self.vitality = vitality
        self.attack = attack
        self.defense = defense

    def save_state(self, memento):
        # 保存状态
        print('\033[35;1m保存当前的状态到备忘录中\033[0m')
        return memento.save_state(self.vitality, self.attack, self.defense)

    def recover_state(self, memento):
        # 恢复状态
        print('\033[36;1m准备恢复备忘录中的状态\033[0m')
        self.vitality = memento.vitality
        self.attack = memento.attack
        self.defense = memento.defense

    def fight(self):
        # 攻击
        pass


class FightCharactor(GameCharacter):
    # 定义一个士兵
    def fight(self):
        self.vitality -= random.randint(1, 10)
        self.attack += random.randint(1, 10)
        self.defense -= random.randint(1, 10)


if __name__ == '__main__':
    memento = Memento()
    a_charactoer = FightCharactor()
    a_charactoer.init_state(100, 90, 80)
    a_charactoer.display_state()

    state = a_charactoer.save_state(memento)
    a_charactoer.fight()
    a_charactoer.display_state()

    a_charactoer.recover_state(state)
    a_charactoer.display_state()
"""
总结：
优点
使用备忘录可以把复杂的对象内部信息对其他的对象屏蔽起来。
缺点
当需要保存的状态数据很大很多时，会消耗较多资源。
"""

