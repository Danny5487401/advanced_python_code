# 我们不使用面向对象的模式，而是使用一个外部的函数来辅助逻辑判断
"""应用
1.中间件，例如接到 请求需要判断是否是正常请求，是否登录了，参数是否合法等，这个时候我们就会用上中间件，
    而中间件就可以用责任链模式来实现， 把handler串成一个串，依次处理，如果已处理完成，那么提前终止，否则进入下一环。
2.责任链模式还有很多处理流程类应用的例子， 比如：请假流程，审批流程，异常处理流程等等
好处：
1.解耦，如果不用责任链模式把处理流程分层，那么就需要一个硕大的函数来处理各种判断，那么这个函数很容易就 臃肿不堪，里面包含各种 if...else...

"""
DEBUG = 0
INFO = 10
WARNING = 100
ERROR = 1000
FATAL = 10000


class BaseLogger:
    def print_log(self, msg):
        raise NotImplementedError("should rewrite this method in Logger")


class DebugLogger(BaseLogger):
    def print_log(self, msg):
        print("DEBUG", msg)


class InfoLogger(BaseLogger):
    def print_log(self, msg):
        print("INFO", msg)


class ErrorLogger(BaseLogger):
    def print_log(self, msg):
        print("ERROR", msg)


class WarningLogger(BaseLogger):
    def print_log(self, msg):
        print("WARNING", msg)


class FatalLogger(BaseLogger):
    def print_log(self, msg):
        print("FATAL", msg)


class Logger:
    def __init__(self):
        self.__loggers = [FatalLogger(), ErrorLogger(), WarningLogger(), InfoLogger(), DebugLogger()]
        self.__levels = [FATAL, ERROR, WARNING, INFO, DEBUG]

    def print_log(self, level, msg):
        for i, lvl in enumerate(self.__levels):
            print(f"trying lvl {lvl}")
            if level == lvl:
                logger = self.__loggers[i]
                logger.print_log(msg)
                return



if __name__ == "__main__":
    Logger().print_log(ERROR, "hello world")
    Logger().print_log(INFO, "hello world")