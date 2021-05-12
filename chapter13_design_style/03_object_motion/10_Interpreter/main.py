
import datetime
import time

"""
解释器模式
解释器模式(Interpreter Pattern):给定一个语言，定义它的文法的一种表示，并定义一个解释器，这个解释器使用该表示来解释语言中的句子.
比如：实现一段简单的中文编程
"""


class Code(object):
    # 自定义语言

    def __init__(self, text=None):
        self.text = text


class InterpreterBase(object):
    # 自定义计算器基类
    def run(self, code):
        pass


class Interpreter(InterpreterBase):
    # 实现解释器方法, 通过表达式字典实现中文编程
    def run(self, code):
        code = code.text
        code_dict = {'获取当前时间戳': time.time(),
                     "获取当前日期": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                     }
        print(code_dict.get(code))


if __name__ == '__main__':
    zw = Code()
    interpreter = Interpreter()
    zw.text = "获取当前时间戳"
    interpreter.run(zw)
    zw.text = "获取当前日期"
    interpreter.run(zw)


"""
总结：
优点：
1、可扩展性比较好，灵活。
2、增加了新的解释表达式的方式。
3、易于实现简单文法。

缺点：
1、可利用场景比较少。
2、对于复杂的文法比较难维护。
3、解释器模式会引起类膨胀。
"""

