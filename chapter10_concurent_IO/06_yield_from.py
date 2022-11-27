# python 3.3添加
from itertools import chain

mylist = [1,2,3]
mydict = {
    "company" : "xiada",
    "name":"danny"
}
def my_chain(*args,**kwargs):
    for my_iterable in args:
        # 方式一
        # for value in my_iterable:
        #     yield value

        # 方式二
        yield from my_iterable
#
# for value in chain(mylist,mydict,range(5,10)):
#     # dict只拿keys
#     print(value)
# 自己实现
# for value in my_chain(mylist,mydict,range(5,10)):
#     # dict只拿keys
#     print(value)


# yield from 与 yield对比
def g1(iterable):
    yield iterable

def g2(iterable):
    # 拿出每个值
    yield from iterable

for value in g1(range(10)):
    print(value)  # range(0, 10)

for value in g2(range(10)):
    print(value)  # 1,2,……,10

def f1(gen):
    yield from gen

# 重点概念：main 为调用方  f1 为委托生成器  gen 为子生成器
# yield from 会在调用方main 与子生成器之间建立一个双向通道

def main():
    f = f1()
    f.send(None)