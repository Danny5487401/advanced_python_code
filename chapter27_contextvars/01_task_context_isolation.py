import asyncio
import contextvars

current_task_name = contextvars.ContextVar("只是一个标识, 用于调试")


async def build_task_message():
    return current_task_name.get() + "~~~"


async def print_task_message(task_name):
    current_task_name.set(task_name)
    print(await build_task_message())


# 目的：演示两个并发协程分别设置同一个 ContextVar 后，读取到的值会按任务隔离。
async def main():
    coro1 = print_task_message("协程1")
    coro2 = print_task_message("协程2")
    await asyncio.gather(coro1, coro2)


asyncio.run(main())

"""
运行结果：
协程1~~~
协程2~~~
"""
