# c10M  如何利用8核心CPU,64GB 内存，在10 gbps网络中保持1000万并发连接

# 问题：1.回调模式编码难度高 2.同步编程的并发性不高 3.多线程编程需要线程间同步,lock
"""
回调之痛：
do_a()
do_b()
如果 b 处理依赖于 a 处理的结果，而 a 过程是异步调用，就不知 a 何时能返回值，需要将后续的处理过程以callback的方式传递给 a ，让 a 执行完以后可以执行 b。代码变化为：
do_a(do_b())
"""


"""解决： 1.采用同步的方式去编写异步的代码 2.采用单线程去切换任务（线程是有操作系统切换的，单线程切换意味着我们需要程序员自己去调度。
不再需要锁，并发性高，如果单线程内切换函数，性能远高于线程切换，并发性高

协程(Co-routine)，即是协作式的例程。
它是非抢占式的多任务子例程的概括，可以允许有多个入口点在例程中确定的位置来控制程序的暂停与恢复执行。
例程是什么？编程语言定义的可被调用的代码段，为了完成某个特定功能而封装在一起的一系列指令。一般的编程语言都用称为函数或方法的代码结构来体现。
"""

def get_url(url):
    # do something1  费时IO操作
    # 要求：此处暂停，切换到另外一个函数执行
    html = get_html(url)

    # parse html  CPU完成解析
    urls = parse_url(html)

def get_url2():
    pass

# 传统函数调用 A->B->C
# 结论：我们需要一个可以暂停的函数，在必要时候恢复函数的执行，所以出现了协程：有多个路口的函数=可以暂停的函数（可以向暂停的地方传入值）
# 生成器可以暂停

def gen_func():
    # 值会传回到生成器内部
    # 这行代码两个作用：产生值，调用方传入值
    html = yield "http://www.baidu.com"
    print(html)
    yield 2
    yield 3
    return "danny"

# 生成器作用
"""
1. 生成器不仅可以产生值，还可以接收值
"""


if __name__ == "__main__":
    gen = gen_func()
    # 启动生成器的两种方式 send,next
    # 方法一：next
    # print(next(gen))
    # print(next(gen))
    # print(next(gen))

    #方法二 :send

    #模拟download
    # 第一次只能是next,不能send 值，会报错: cannot send non-None Value to a just-started gennerator,刚开始没有执行到yield那行代码
    # 所以 再调用send 发送一个非none值之前，哦们必须启动一次生成器，方式有两种
    # 第一次需要send None ，启动方法一
    url = gen.send(None)
    # 启动方法二
    # url = next(gen)

    print(url)
    html = "input danny"
    # send方法传入值到生成器内部，同时还可以重启生成器到下一个yield位置
    print(gen.send(html))
