import asyncio
import contextvars

current_task_name = contextvars.ContextVar("只是一个标识, 用于调试", default="哼哼")


async def build_task_message():
    return current_task_name.get() + "~~~"


async def print_default_message(task_name):
    print(await build_task_message())


# 目的：演示 ContextVar 配置默认值后，即使没有显式 set 也可以读取默认值。
async def main():
    coro1 = print_default_message("协程1")
    coro2 = print_default_message("协程2")
    await asyncio.gather(coro1, coro2)


asyncio.run(main())

"""
运行结果：
哼哼~~~
哼哼~~~
"""
