# c10k 1GHz CPU 2G内存，1gbps，让单台服务器同时为1万个客户端提供FTP服务

""" Unix下五种I/O模型
发展趋势
1.阻塞式IO
2.非阻塞式IO
3.IO多路复用  ：比较成熟，稳定
4.信号驱动IO  ：比较少
5.异步IO（posix的aio_系列函数）
"""

# io多路复用：select 阻塞
"""
select,poll,epoll都是IO多路复用机制，IO多路复用就是通过一种机制，一个进程可以监听多个描述符，一旦某个描述符就绪，一般是
读就绪或者写就绪，能够通知程序就行相应的读写操作。但select,poll,epoll本质上都是同步IO，因为他们都需要在读写事件就绪后自己
负责进行读写，也就是说整个读写过程是阻塞的，而异步IO则无需自己进行读写，异步IO的实现会负责把数据从内核拷贝到用户空间。

epoll:采用红黑树的数据结构
"""

# 结论
"""
epoll并不一定比select好

1.在高并发的情况下，连接活跃度不高的情况，epoll比select好     比如网站，连接之后随时可能断开
2.并发性不是很高，连接活跃度比较高，select比epoll好        比如游戏，很少断开
"""
from urllib.parse import urlparse
import socket
import select

# 不使用select.select()   select(rlist, wlist, xlist, timeout=None)
# 使用selctor,包装的更好用，会根据平台自动选择slect,poll,epoll
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
    client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 设置非阻塞
    client.setblocking(False)
    try:
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好，需要while不挺的去检查状态
    # 做计算任务或者再次发起其他的连接需求
    # 连接还没准备好OSerror,依赖上一步的连接状态
    while True:
        try:
            client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
            break
        except OSError as e:
            pass

    data = b''
    while True:
        try:
            d = client.recv(1024)
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

# 方法二
# 使用select完成http请求
# 回调编写难
# 全局变量
selector = DefaultSelector()
stop = False
urls = ["http://www.baidu.com"]

class Fetcher:
    def connected(self, key):
        # 取消注册事件
        selector.unregister(key.fd)
        # 已经是就绪状态了
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))

        #注册可读事件
        selector.register(self.client.fileno(),EVENT_READ, self.readable)

    def readable(self, key):
        d = self.client.recv(1024)
        if d:
            self.data += d
        else:
            # 代表数据读完
            selector.unregister(key.fd)
            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
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
        selector.register(self.client.fileno(),EVENT_WRITE, self.connected)

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
            callback_func = key.data
            callback_func(key)


if __name__ == "__main__":
    # 方法一：
    # get_url("http://www.baidu.com")

    # 方法二
    fetcher = Fetcher()
    fetcher.get_html("http://www.baidu.com")
    # 事件循环
    loop()
