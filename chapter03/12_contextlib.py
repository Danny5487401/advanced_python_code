# 不想生成一个class
import contextlib

# 必须是一个生成器
@contextlib.contextmanager
def file_open(file_name):
    print("file open")
    # yield之前理解成enter
    yield {}
    # yield 之后理解成exit
    print("file end")


with file_open("danny") as f:
    print("file procesing")
