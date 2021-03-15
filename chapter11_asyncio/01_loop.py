#事件循环 + 回调（在asyncio中是驱动生成器） + IO多路复用
# asyncio是python用于解决IO编程的一整套解决方法 tornado ,gevent,twisted(scrapy,django channels用于http2.0开发)

# tornado（实现了web服务器,可以直接部署，+nginx),django+Flask(web框架，不提供服务器，需要uwsgi,gunicorn,nginx)
# tornado的数据库驱动是不同的，需要一异步的

import asyncio
import time

async def get_html(url):
    print("start get url")
    # 异常的两种方式
    # asyncio.sleep(2) #RuntimeWarning: coroutine 'sleep' was never awaited
    # await time.sleep(2) # object NoneType can't be used in 'await' expression
    # time.sleep(2) # 不会报错，但不能用 否则会20s，因为在loop中发现是同步操作，而asyncio.sleep(2)是立即返回对象

    # 正确方式
    await asyncio.sleep(2)

    print("end get url")

# 带返回值
async def get_html1(url):
    print("start get url")
    # 正确方式
    await asyncio.sleep(2)

    return "danny"

# def call_back(): 等于call_back(future)
# 默认无参数的情况
def call_back(future):
    # 假设完成后发送邮件等需求
    print("send email to danny")

# 有参数  使用偏函数传递参数，重新生成函数
from functools import partial
#错误写法，参数必须写在前面
# def call_back_param(future,url):
def call_back_param(url, future):
    # 假设完成后发送邮件等需求
    print("from {} send email to danny" .format(url))

if __name__ == "__main__":
    # 无返回值
    # start_time = time.time()
    # # 完成select操作
    # loop = asyncio.get_event_loop()


    # # 多个运行
    # tasks = [get_html("www.baidu.com") for i in range(10)]
    # loop.run_until_complete(asyncio.wait(tasks))

    # # 阻塞的方法
    # # 单个运行
    # # loop.run_until_complete(get_html("www.baidu.com")) # 可以接受协程类型

    # print("last time {}" .format(time.time()-start_time))



    # 带返回值操作
    start_time = time.time()
    loop = asyncio.get_event_loop()
    # 两种方式 1. loop.create_task()  2. asyncio.ensure_future()
    # task是future类型的子类，以下用法是一样的
    # 方式一 ：
    tasks = loop.create_task(get_html1("www.baidu.com"))
    # 添加回调函数 传递无参数
    tasks.add_done_callback(call_back)  # call_back() takes 0 positional arguments but 1 was given，因为call_back()默认传递了future
    #  添加回调函数 传递参数
    tasks.add_done_callback(partial(call_back_param,"www.baidu.com"))

    loop.run_until_complete(tasks)
    print("返回结果是{}" .format(tasks.result()))     # 最终结果先发送邮件再返回结果


    # 方式二
    # get_future = asyncio.ensure_future(get_html1("www.baidu.com"))  # 内部还是调用loop.create_task，返回task类型
    # loop.run_until_complete(get_future)  # 可以接受future类型
    # print(get_future.result())

    print("last time {}" .format(time.time()-start_time))

