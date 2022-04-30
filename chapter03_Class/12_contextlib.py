# 不想生成一个class
import contextlib

"""
@contextlib.contextmanager 是一个装饰器，由它修饰的方法会有两部分构成，中间由 yield 关键字分开。
    但是contextmanager只是省略了 __enter__() / __exit__() 的编写，但并不负责实现资源的“获取”和“清理”工作；
    “获取”操作需要定义在 yield 语句之前，“清理”操作需要定义 yield 语句之后，这样 with 语句在执行 __enter__() / __exit__() 方法时会执行这些语句以获取/释放资源。

"""


# 必须是一个生成器
@contextlib.contextmanager
def file_open(file_name):
    # 打开文件和关闭文件是IO操作，还有数据库链接之类
    print("file open")
    # yield之前理解成enter
    yield {}
    # yield 之后理解成exit
    print("file end")


with file_open("danny") as f:
    print("file procesing")
