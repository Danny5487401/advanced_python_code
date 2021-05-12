
"""
状态模式
当控制一个对象的状态转换的条件表达式过于复杂时,把状态的判断逻辑转移到表示不同状态的一系列类当中,
这可以把复杂的判断逻辑简化
"""


class State(object):
    """定义一个状态基类"""

    def toggle_amfm(self):
        # 定义一个切换状态方法
        pass

    def scan(self):
        pass


class AMState(State):
    # 定义一个AM频道类
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["1250", "1380", "1510"]
        self.pos = 0
        self.name = "AM"

    def scan(self):
        # 定义一个共用的方法，扫描刻度盘下一个状态
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("扫描中...状态是", self.stations[self.pos], self.name)

    def toggle_amfm(self):
        # 定义一个切换AM/FM频道的方法
        print("转换到FM频道")
        self.radio.state = self.radio.fm_state


class FMState(State):
    # 定义一个FM频道类
    def __init__(self, radio):
        self.radio = radio
        self.stations = ["81.3", "89.1", "103.9"]
        self.pos = 0
        self.name = "FM"

    def scan(self):
        # 定义一个共用的方法，扫描刻度盘下一个状态
        self.pos += 1
        if self.pos == len(self.stations):
            self.pos = 0
        print("扫描中...状态是", self.stations[self.pos], self.name)

    def toggle_amfm(self):
        # 定义一个切换AM/FM频道的方法
        print("转换到AM频道")
        self.radio.state = self.radio.am_state


class Radio(object):
    # 定义一个收音机,有一个扫描按钮，和切换AM/Fm的开关
    def __init__(self):
        self.am_state = AMState(self)
        self.fm_state = FMState(self)
        self.state = self.am_state

    def toggle_amfm(self):
        self.state.toggle_amfm()

    def scan(self):
        self.state.scan()


if __name__ == '__main__':
    radio = Radio()
    actions = [radio.scan] * 2 + [radio.toggle_amfm] + [radio.scan] * 2
    actions = actions * 2
    for action in actions:
        action()

"""
总结：
就是通过一个对象的方法调用已经存在其他类对象的状态
"""

