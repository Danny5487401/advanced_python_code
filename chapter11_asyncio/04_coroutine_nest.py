# 协程嵌套协程  见时序图
# 官方代码

import asyncio


async def compute(x, y):
    print("Compute %s + %s ..." % (x, y))
    await asyncio.sleep(1.0)
    return x + y


async def print_sum(x, y):
    # 使用 await 方法会驱动协程 compute() 执行, 并得到其返回值
    result = await compute(x, y)
    print("%s + %s = %s" % (x, y, result))


if __name__ == "__main__":
    # 一个协程驱动另一个协程执行，并等待其返回结果

    loop = asyncio.get_event_loop()
    loop.run_until_complete(print_sum(1, 2))
    loop.close()
