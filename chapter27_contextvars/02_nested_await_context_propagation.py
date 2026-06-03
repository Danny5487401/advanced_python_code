import asyncio
import contextvars

current_task_name = contextvars.ContextVar("只是一个标识, 用于调试")


async def build_task_message():
    return current_task_name.get() + "~~~"


async def build_message_through_nested_call():
    return await build_task_message()


async def print_nested_and_direct_message(index, task_name):
    current_task_name.set(task_name)
    print(index, await build_message_through_nested_call())
    print(index, await build_task_message())


# 目的：演示 ContextVar 的值可以在同一个任务的嵌套 await 调用链中继续传递。
async def main():
    coro1 = print_nested_and_direct_message(1, "协程1")
    coro2 = print_nested_and_direct_message(2, "协程2")
    await asyncio.gather(coro1, coro2)


asyncio.run(main())

"""
运行结果：
1 协程1~~~
1 协程1~~~
2 协程2~~~
2 协程2~~~
"""
