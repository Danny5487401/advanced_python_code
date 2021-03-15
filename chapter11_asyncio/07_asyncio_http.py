# asyncio不提供http接口，更底层提供了tcp，可以使用aiohttp

import asyncio
from urllib.parse import urlparse
import socket


# 阻塞的函数
async def get_url(url):
    # 通过socket请求url
    url = urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    # client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # # 设置非阻塞
    # client.setblocking(False)
    # try:
    #     client.connect((host, 80))
    # except BlockingIOError as e:
    #     pass

    reader, writer = await asyncio.open_connection(host,80)


    # 不停的询问连接是否建立好，需要while不挺的去检查状态
    # 做计算任务或者再次发起其他的连接需求
    # 连接还没准备好OSerror,依赖上一步的连接状态
    # while True:
    #     try:
    #         client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))
    #         break
    #     except OSError as e:
    #         pass

    writer.write("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(path, host).encode("utf8"))

    all_lines = []
    async for raw_line in reader:
        data = raw_line.decode("utf8")
        all_lines.append(data)
    html = "" .join(all_lines)
    html = html.split("\r\n\r\n")[1]
    # print(html)
    return html
    # data = b''
    # while True:
    #     try:
    #         d = client.recv(1024)
    #     except BlockingIOError as e:
    #         continue
    #     else:
    #         if d:
    #             data += d
    #         else:
    #             break
    #
    # data = data.decode("utf8")
    # html_data = data.split("\r\n\r\n")[1]

    # print(html_data)
    # client.close()

async def main(loop):
    tasks = []
    url1 = "http://www.baidu.com"
    url2 = "http://www.soso.com"
    url3 = "http://news.baidu.com/"
    tasks.append(asyncio.ensure_future(get_url(url1)))
    tasks.append(asyncio.ensure_future(get_url(url2)))
    tasks.append(asyncio.ensure_future(get_url(url3)))
    for task in asyncio.as_completed(tasks):
        result = await task
        print(result)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # task = get_url("http://www.baidu.com")
    # loop.run_until_complete(task)

    # 获取返回结果
    # task = asyncio.ensure_future(get_url("http://www.baidu.com"))
    # loop.run_until_complete(task)
    # print(task.result())

    # 完成一个打印一个
    loop.run_until_complete(main(loop))
