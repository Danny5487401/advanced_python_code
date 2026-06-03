import asyncio
import contextvars

current_task_name = contextvars.ContextVar("只是一个标识, 用于调试")


async def build_task_message():
    return current_task_name.get() + "~~~"


async def reset_context_and_build_message():
    current_task_name.set("重新设置")
    return await build_task_message()


async def print_message_before_and_after_reset(index, task_name):
    current_task_name.set(task_name)
    print(index, await build_task_message())
    print(index, await reset_context_and_build_message())
    print(index, await build_task_message())


# 目的：演示同一任务内部重新设置 ContextVar 后，后续读取会得到新值，同时不影响其他任务。
async def main():
    coro1 = print_message_before_and_after_reset(1, "协程1")
    coro2 = print_message_before_and_after_reset(2, "协程2")
    await asyncio.gather(coro1, coro2)


asyncio.run(main())

"""
运行结果：
1 协程1~~~
1 重新设置~~~
1 重新设置~~~
2 协程2~~~
2 重新设置~~~
2 重新设置~~~
"""
