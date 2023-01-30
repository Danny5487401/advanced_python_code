# 多进程：耗CPU操作，进程切换对于操作系统来说代价比多线程高
# 多线程：io操作

# 计算：cpu 图形处理 挖矿（b特币)

from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor
import time


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


def random_sleep(n):
    time.sleep(n)
    return n


# 多线程
# if __name__ == "__main__":
# 对于cpu操作
# 多线程
# with ThreadPoolExecutor(max_workers=3) as executor:
#     all_tasks = [executor.submit(fib, (num)) for num in range(25,35) ]
#     start_time = time.time()
#     for future in as_completed(all_tasks):
#         data = future.result()
#         print("exe result {}" .format(data))
#     print("last time is :{}" .format(time.time()-start_time))

# 多进程
#     with ProcessPoolExecutor(max_workers=3) as executor:
#         all_tasks = [executor.submit(fib, (num)) for num in range(25,35) ]
#         start_time = time.time()
#         for future in as_completed(all_tasks):
#             data = future.result()
#             print("exe result {}" .format(data))
#         print("last time is :{}" .format(time.time()-start_time))

# 对于IO操作
if __name__ == "__main__":
    # 多线程
    # with ThreadPoolExecutor(max_workers=3) as executor:
    #     all_tasks = [executor.submit(random_sleep, (num)) for num in [2]*30 ]
    #     start_time = time.time()
    #     for future in as_completed(all_tasks):
    #         data = future.result()
    #         print("exe result {}" .format(data))
    #     print("last time is :{}" .format(time.time()-start_time))

    # 多进程
    with ProcessPoolExecutor(max_workers=3) as executor:
        all_tasks = [executor.submit(random_sleep, (num)) for num in [2] * 30]
        start_time = time.time()
        for future in as_completed(all_tasks):
            data = future.result()
            print("exe result {}".format(data))
        print("last time is :{}".format(time.time() - start_time))
