import asyncio

def callback(sleep_time):
    print("sleep {} success"  .format(sleep_time))

def stop_loop(loop):
    loop.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    #call_soon使用
    # # 直接插入函数，不是协程
    # loop.call_soon(callback,2)  # 下一个循环中即可执行
    #
    # # loop.run_until_complete()     # 不能用run_until_complete,因为不是协程
    # # loop.run_forever()  #不会停止


    # # 需要停止loop的时候
    # loop.call_soon(stop_loop,loop)
    # loop.run_forever()


    # call_later 源码在base_events
    # 不会根据添加顺序执行,根据时间排序
    # loop.call_later(3,callback,3)
    # loop.call_later(1,callback,1)
    # loop.call_later(2,callback,2)
    # loop.call_soon(callback,4)  # 优先于call_later
    # # loop.call_soon(stop_loop, loop)
    # loop.run_forever()


    # call_at 使用
    # 使用内部时间,不会根据添加顺序执行,根据时间排序
    now = loop.time()
    loop.call_at(now+2,callback,2)
    loop.call_at(now+1,callback,1)
    loop.call_at(now+3,callback,3)
    loop.call_soon(callback, 4)
    loop.run_forever()

    # 可以在多线程中使用
    # loop.call_soon_threadsafe()使用  ：线程安全
    loop.call_soon_threadsafe()