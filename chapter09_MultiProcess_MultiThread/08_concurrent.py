# python3.2引入
# 线程池，理解协程才容易
from concurrent.futures import ThreadPoolExecutor,as_completed,wait
# 理解futures:未来对象，task是返回容器
from concurrent.futures import Future


# 主线程获取某一个线程的状态，以及返回值
# 1.当一个线程完成后，主线程马上知道并获取返回值
# 2.futures让多线程和多进程编码接口一致，与java的futures设计理念相近
import time
def get_html(sleep_time):
    time.sleep(sleep_time)
    print("get page{}success" .format(sleep_time))
    return sleep_time


executor = ThreadPoolExecutor(max_workers=2)
# 通过submit提交将要执行的函数到线程池中,submit是立即返回
# task1 = executor.submit(get_html, (3))
# task2 = executor.submit(get_html, (2))

# # 判断执行状态是否成功
# print(task1.done())
# # 执行中取消不了
# print(task2.cancel())
# time.sleep(3)
# print(task1.done())
# # 获取task的执行结果
# print(task1.result())

# 获取已经成功的task的返回
# as_completed是生成器
urls = [8,3,5,6,7] # 睡眠好几种，模拟

# 方法一
all_tasks = [executor.submit(get_html, (url)) for url in urls]
# 等待所有任务完成,默认全部完成
# wait 注意return_when
# wait(all_tasks)
# print("all finished")
wait(all_tasks, return_when='FIRST_COMPLETED')
print("first finished")

# for future in as_completed(all_tasks):
#     data = future.result()
#     print("get future_page {} success" .format(data))

# 通过excutor获取已经完成的tasks
# 方法二
# 返回的直接是data
# for data in executor.map(get_html, urls):
#     # 打印是顺序的
#     print("get future_page {} success" .format(data))
