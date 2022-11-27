# python3.5之后
# python为了将语义变得更加明确，引入async和await关键词来定义原生的协程，区分生成器和协程，之前两者混合使用
# 方式一
async def downloader(url):
    return "danny"

# await 后面加awaitable对象
from collections import Awaitable  # 实现__await__
import types

# 加协程装饰器
@types.coroutine
def downloader2(url):
    return "danny"

async def download_url(url):
    # dosomething
    # html = await downloader(url)
    # 方式二
    html = downloader2(url)

    return html

if __name__ == "__main__":
    coro = download_url("http://www.baidu.com")
    # 不能这样调用
    # next(None) #coroutine 'download_url' was never awaited

    # 需要这样调用
    coro.send(None)