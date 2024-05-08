# asyncio是异步解决方案

# 在线程中集成阻塞IO

import asyncio
from urllib.parse import urlparse
import socket
from concurrent.futures import ThreadPoolExecutor


# 阻塞的函数
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
        client.connect((host, 80))
    except BlockingIOError as e:
        pass

    # 不停的询问连接是否建立好，需要while不挺的去检查状态
    # 做计算任务或者再次发起其他的连接需求
    # 连接还没准备好OSerror,依赖上一步的连接状态
    while True:
        try:
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
            d = client.recv(1024)
        except BlockingIOError as e:
            continue
        else:
            if d:
                data += d
            else:
                break

    data = data.decode("utf8")
    print(data)
    html_data = data.split("\r\n\r\n")[1]
    print(html_data)
    client.close()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    executor = ThreadPoolExecutor()
    # 马山返回
    task = loop.run_in_executor(
        executor, get_url, "http://www.baidu.com"
    )  # 源码在base_events.py
    loop.run_until_complete(task)
