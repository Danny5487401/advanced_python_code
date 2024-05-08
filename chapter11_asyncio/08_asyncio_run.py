import asyncio


async def coroutine():
    print("in coroutine")


if __name__ == "__main__":

    c = coroutine()
    # asyncio.run 内部包含了创建事件循环、执行协程、关闭事件循环等一套逻辑
    asyncio.run(c)
