
"""
命令模式
结构组成：
命令角色，具体命令角色，接收者角色，请求者（调用者）角色（Invoker），客户角色（Client）
"""
import abc


class Command(metaclass=abc.ABCMeta):
    # 命令抽象类
    @abc.abstractmethod
    def execute(self):
        # 命令对象对外只提供execute方法
        pass


class VmReciver(object):
    # 命令接收者，真正执行命令的地方

    def start(self):
        print("启动虚拟机")

    def stop(self):
        print("关闭虚拟机")


class StartVmCommand(Command):
    # 具体命令角色：开启虚拟机的命令
    def __init__(self, recevier):
        self.recevier = recevier

    def execute(self):
        # 真正执行命令的时候命令接收者开启虚拟机
        self.recevier.start()


class StopVmCommand(Command):
    # 具体命令角色：关闭虚拟机的命令
    def __init__(self, recevier):
        self.recevier = recevier

    def execute(self):
        # 真正执行命令的时候命令接收者开启虚拟机
        self.recevier.stop()


class ClientInvoker(object):
    # 请求者（调用者）角色,客户角色
    def __init__(self, command):
        self.command = command

    def do(self):
        self.command.execute()


if __name__ == '__main__':
    recevier = VmReciver()  # 创建接收者角色
    start_command = StartVmCommand(recevier)  # 创建一个开启虚拟机命令
    client = ClientInvoker(start_command)  # 创建一个调用者角色
    client.do()

    # 调用其它命令
    stop_command = StopVmCommand(recevier)
    client.command = stop_command
    client.do()
"""
总结：
优点：
降低对象之间的耦合度。
新的命令可以很容易地加入到系统中。
可以比较容易地设计一个组合命令。
调用同一方法实现不同的功能
缺点：
使用命令模式可能会导致某些系统有过多的具体命令类。
因为针对每一个命令都需要设计一个具体命令类，因此某些系统可能需要大量具体命令类，这将影响命令模式的使用。
"""

