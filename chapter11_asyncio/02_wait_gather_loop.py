# wait 和gather
import time
import asyncio

# 带返回值
async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    return "danny"

# def call_back(): 等于call_back(future)
# 默认无参数的情况
def call_back(future):
    # 假设完成后发送邮件等需求
    print("send email to danny")



if __name__ == "__main__":
    # 带返回值操作
    # start_time = time.time()
    # loop = asyncio.get_event_loop()
    # tasks = [get_html("www.baidu.com") for i in range(10)]
    #
    # # wait 方式
    # # loop.run_until_complete(asyncio.wait(tasks))
    #
    # # gather 方式
    # loop.run_until_complete(asyncio.gather(*tasks))
    #
    # print("last time {}" .format(time.time()-start_time))

    # 结论
    """
    gather是higher level，可以将tasks分组
    
    """

    loop = asyncio.get_event_loop()
    # 方式一
    # group1 = [get_html("www.taobao.com") for i in range(2)]
    # group2 = [get_html("www.jd.com") for i in range(2)]
    # loop.run_until_complete(asyncio.gather(*group1,*group2))

    # 方式二
    group1 = [get_html("www.taobao.com") for i in range(2)]
    group2 = [get_html("www.jd.com") for i in range(2)]
    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)
    loop.run_until_complete(asyncio.gather(group1,group2))
