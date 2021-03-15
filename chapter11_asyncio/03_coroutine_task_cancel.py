# 1. loop.run_until_complete()  可以停止运行，源码在 base_events.py

import asyncio

# loop = asyncio.get_event_loop()
# 永久运行
# loop.run_forever()
# loop.run_until_complete()

# loop放在future中，future又放在loop中，逻辑有点混乱
# 取消 future(tasks)

# 场景：某种情况下下载失败后取消任务
async def get_url(sleep_time):
    print("waiting")
    await asyncio.sleep(sleep_time)
    print("done after {} s" .format(sleep_time))


if __name__ == "__main__":
    task1 = get_url(1)
    task2 = get_url(2)
    task3 = get_url(3)
    tasks = [task1,task2,task3]
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e: # ctrl +c
        all_tasks = asyncio.Task.all_tasks()  # 源码tasks.py
        for task in all_tasks:
            print("cancel task")
            print(task.cancel())
        loop.stop()
        # 一定要再启动
        loop.run_forever()
    finally:
        # 关闭
        loop.close()  # 源码在 base_events.py， 做的事比stop()多
