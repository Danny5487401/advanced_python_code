import asyncio


async def coroutine():
    print("in coroutine")
    return "result"


if __name__ == "__main__":
    # 协程有返回值
    loop = asyncio.get_event_loop()
    c = coroutine()
    result = loop.run_until_complete(c)
    print(result)
    """
    in coroutine
    result
    """
    loop.close()

    # 对于 asyncio.run 而言也是一样的
    c = coroutine()
    result = asyncio.run(c)
    print(result)
    """
    in coroutine
    result
    """
