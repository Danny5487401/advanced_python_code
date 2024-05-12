# python3.2 引入 线程池，理解协程才容易
from concurrent.futures import ThreadPoolExecutor, wait

# 理解futures:未来对象，task是返回容器

# 主线程获取某一个线程的状态，以及返回值
# 1.当一个线程完成后，主线程马上知道并获取返回值
# 2.futures让多线程和多进程编码接口一致，与java的futures设计理念相近
import time


# 2 定义一个普通函数作为线程任务。
def get_html(sleep_time):
    time.sleep(sleep_time)
    print("get page{} success".format(sleep_time))
    return sleep_time


if __name__ == "__main__":
    # 1 调用 ThreadPoolExecutor 类的构造器创建一个线程池。
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
    urls = [8, 3, 5, 6, 7]  # 睡眠好几种，模拟

    # 3 调用 ThreadPoolExecutor 对象的 submit() 方法来提交线程任务
    # 方法一 submit 方法会返回一个 Future 对象，Future 类主要用于获取线程任务函数的返回值
    all_tasks = [executor.submit(get_html, (url)) for url in urls]
    # 等待所有任务完成,默认全部完成
    # wait 注意return_when
    # wait(all_tasks)
    # print("all finished")
    wait(all_tasks, return_when="FIRST_COMPLETED")
    print("first finished")

    # for future in as_completed(all_tasks):
    #     data = future.result()
    #     print("get future_page {} success" .format(data))

    # 通过executor获取已经完成的tasks
    # 方法二 map
    # 返回的直接是data
    # for data in executor.map(get_html, urls):
    #     # 打印是顺序的
    #     print("get future_page {} success" .format(data))

    # 4 当不想提交任何任务时，调用 ThreadPoolExecutor 对象的 shutdown() 方法来关闭线程池。
    executor.shutdown()
