from urllib.parse import urlparse
import socket

import select

# 不使用select.select()   select(rlist, wlist, xlist, timeout=None)
# 使用selector,包装的更好用，会根据平台自动选择select,poll,epoll/kqueue
from selectors import DefaultSelector, EVENT_READ, EVENT_WRITE


# 方法一
# 通过非阻塞式IO实现HTTP请求：需要不断地while循环
def get_url(url):
    # 通过socket请求url
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 设置非阻塞
    client.setblocking(False)
    try:
        client.connect((host, 80))  # 在默认情况下是阻塞的
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好，需要while不挺的去检查状态
    # 做计算任务或者再次发起其他的连接需求
    # 连接还没准备好OSerror,依赖上一步的连接状态
    while True:
        try:
            # 注：client.send()函数并不会阻塞太久，它只负责将请求数据拷贝到TCP/IP协议栈的系统缓冲区中就返回，并不等待服务端返回的应答确认
            # send不发生异常，则发送完成
            client.send(
                "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
                    path, host
                ).encode("utf8")
            )
            break
        except OSError as e:
            pass

    data = b""
    while True:
        try:
            d = client.recv(1024)  # 在默认情况下是阻塞的
        except BlockingIOError as e:
            continue
        else:
            if d:
                data += d
            else:
                break

    data = data.decode("utf8")
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


"""
分析：判断非阻塞调用是否就绪如果 OS 能做，是不是应用程序就可以不用自己去等待和判断了，就可以利用这个空闲去做其他事情以提高效率。
    所以OS将I/O状态的变化都封装成了事件，如可读事件、可写事件。并且提供了专门的系统模块让应用程序可以接收事件通知。这个模块就是select。
    让应用程序可以通过select注册文件描述符和回调函数。当文件描述符的状态发生变化时，select 就调用事先注册的回调函数。
    select因其算法效率比较低，后来改进成了poll，再后来又有进一步改进，BSD内核改进成了kqueue模块，
    而Linux内核改进成了epoll模块。这四个模块的作用都相同，暴露给程序员使用的API也几乎一致，区别在于kqueue 和 epoll 在处理大量文件描述符时效率更高

"""
# 方法二  改进
# 使用select完成http请求
# 把I/O事件的等待和监听任务交给了 OS，那 OS 在知道I/O状态发生改变后（例如socket连接已建立成功可发送数据），它又怎么知道接下来该干嘛呢？只能回调
# 回调编写难
# 全局变量


selector = DefaultSelector()
stop = False
urls = ["http://www.baidu.com"]


class Fetcher:
    def connected(self, key):
        # 连接后做的事

        # 取消注册事件
        selector.unregister(key.fd)
        # 已经是就绪状态了
        self.client.send(
            "GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(
                self.path, self.host
            ).encode("utf8")
        )

        # 注册可读事件
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):
        # 可读后做的事

        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            # 代表数据读完
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            # print(html_data)
            self.client.close()
            urls.remove(self.spider_url)
            if not urls:
                # 全局变量
                global stop
                stop = True

    def get_html(self, url):
        # 解析url
        self.spider_url = url
        url_parse = urlparse(url)
        self.data = b""
        self.host = url_parse.netloc
        self.path = url_parse.path
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置非阻塞
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))
        except BlockingIOError as e:
            pass

        # 注册到selector中  注意是文件描述符，因为要接下来发送send，所以注册write事件,然后回调函数
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)


# 需要自己去调用回调，不是系统自动的
def loop():
    """
    事件循环，不停的请求socket的状态并调用对应的函数   如twister,tornado,gevent,asyncio 回调+时间循环+select（poll,epoll)

    :return:
    """
    #  1. select本身是不支持register模式的，selector封装了才行
    # 2. socket状态变化后的回调是由程序员来完成的
    # 看源码得知selector.select()返回ready ,他是list中包含tuple
    # while True:
    while not stop:
        #  r, w, x = select.select(r, w, w, timeout) OSError: [WinError 10022] 提供了一个无效的参数。
        # windows情况下不能为空，linux情况下可以
        ready = selector.select()
        for key, mask in ready:
            # print(key,"---",mask,"\n") # SelectorKey(fileobj=540, fd=540, events=2, data=<bound method Fetcher.connected of <__main__.Fetcher object at 0x0000017036F85708>>) --- 2
            callback_func = key.data
            callback_func(key)


if __name__ == "__main__":
    # 方法一：
    # get_url("http://www.baidu.com")
    """
    结果：一是耗时与同步阻塞相当，二是代码更复杂
    分析： 虽然 connect() 和 recv() 不再阻塞主程序，空出来的时间段CPU没有空闲着，但并没有利用好这空闲去做其他有意义的事情，
        而是在循环尝试读写 socket （不停判断非阻塞调用的状态是否就绪）。还得处理来自底层的可忽略的异常。也不能同时处理多个 socket 。

    """

    # 方法二
    fetcher = Fetcher()
    fetcher.get_html("http://www.baidu.com")
    # 事件循环
    loop()
