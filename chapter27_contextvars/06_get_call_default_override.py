import asyncio
import contextvars

current_task_name = contextvars.ContextVar("只是一个标识, 用于调试", default="哼哼")


async def build_message_with_call_default():
    return current_task_name.get("哈哈") + "~~~"


async def print_call_default_message(task_name):
    print(await build_message_with_call_default())


# 目的：演示 ContextVar.get(default) 传入的临时默认值会优先于变量创建时配置的默认值。
async def main():
    coro1 = print_call_default_message("协程1")
    coro2 = print_call_default_message("协程2")
    await asyncio.gather(coro1, coro2)


asyncio.run(main())

"""
运行结果：
哈哈~~~
哈哈~~~
"""
