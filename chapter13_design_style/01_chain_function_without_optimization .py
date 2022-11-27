"""
责任链模式在面向对象程式设计里是一种软件设计模式，它包含了一些命令对象和一系列的处理对象。
    每一个处理对象决定它能处理哪些命令对象，它也知道如何将它不能处理的命令对象传递给该链中的下一个处理对象
    所以其实它就像一个工厂流水线，我们把原料丢进去，每一层处理一部分，如果处理完成，就退出，没有完成，就进入下一个环节
"""

"""
# 案例：打印日志的一个例子，打印日志通常是按照优先级，当设定一个阈值之后，高于这个等级的日志才会打印，否则不打印， 通常优先级从高到低依次是：
1. FATAL/PANIC
2. ERROR
3. WARNING
4. INFO
5. DEBUG
"""

DEBUG = 0
INFO = 10
WARNING = 100
ERROR = 1000
FATAL = 10000


class Logger:
    def __init__(self):
        self.next = None

    def set_next(self, next):
        self.next = next
        return next

    def print(self, level, msg):
        raise NotImplementedError("should rewrite this method in Logger")

class DebugLogger(Logger):
    def print(self, level, msg):
        if level == DEBUG:
            print("DEBUG", msg)
            return

        if self.next:
            print("not handled by DebugLogger")
            self.next.print(level, msg)

class InfoLogger(Logger):
    def print(self, level, msg):
        if level == INFO:
            print("INFO", msg)
            return

        if self.next:
            print("not handled by InfoLogger")
            self.next.print(level, msg)

class WarningLogger(Logger):
    def print(self, level, msg):
        if level == WARNING:
            print("WARNING", msg)
            return

        if self.next:
            print("not handled by WarningLogger")
            self.next.print(level, msg)

class ErrorLogger(Logger):
    def print(self, level, msg):
        if level == ERROR:
            print("ERROR", msg)
            return

        if self.next:
            print("not handled by ErrorLogger")
            self.next.print(level, msg)

class FatalLogger(Logger):
    def print(self, level, msg):
        if level == FATAL:
            print("FATAL", msg)
            return

        if self.next:
            print("not handled by FatalLogger")
            self.next.print(level, msg)


if __name__ == "__main__":
    logger = FatalLogger()
    logger.set_next(ErrorLogger()).set_next(WarningLogger()).set_next(InfoLogger()).set_next(DebugLogger())

    logger.print(INFO, "info")
    logger.print(DEBUG, "debug")

# 责任链模式的几个核心特点
# 1分层处理
# 2当层没处理完成的，放下一层继续处理
# 3可以把各个处理函数(handler)串成一个链