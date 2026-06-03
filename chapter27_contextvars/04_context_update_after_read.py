import asyncio
import contextvars

current_task_name = contextvars.ContextVar("只是一个标识, 用于调试")


async def build_message_then_update_context():
    message = current_task_name.get() + "~~~"
    current_task_name.set("重新设置啦")
    return message


async def build_message_through_nested_call():
    return await build_message_then_update_context()


async def print_message_and_updated_context(task_name):
    current_task_name.set(task_name)
    print(await build_message_through_nested_call())
    print(current_task_name.get())


# 目的：演示读取旧值后再更新 ContextVar，调用方随后能看到更新后的上下文值。
async def main():
    coro1 = print_message_and_updated_context("夏色祭")
    await coro1


asyncio.run(main())

"""
运行结果：
夏色祭~~~
重新设置啦
"""
