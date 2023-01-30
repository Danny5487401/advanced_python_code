# linux上运行

# import os
# import time
# # 新建子进程，fork只能用在Linux系统
# pid = os.fork()
# # 注意fork在打印的前后顺序
# print("danny")
# if pid == 0: # 代表子进程
#     print("子进程是{},父进程是{}" .format(os.getpid(),  os.getppid()))
# else:
#     print("我是父进程：{} .format(pid)")
# # 注意睡眠的作用：确定主进程是否退出
#
# time.sleep(2)

# 更推荐
from concurrent.futures import ProcessPoolExecutor

# ProcessPoolExcutor 底层使用multiprocessing
import multiprocessing
import time


def get_html(n):
    time.sleep(n)
    print("sub process success")
    return n


if __name__ == "__main__":
    # process = multiprocessing.Process(target=get_html,args=(6,))
    # # 未启动前
    # print(process.pid)
    # process.start()
    # # 启动后
    # print(process.pid)
    # process.join()
    # print("main process end")

    # 使用Multiprocess进程池
    pool = multiprocessing.Pool()  # 默认CPU数量

    # result = pool.apply_async(get_html,args=(3,))
    #
    # # 等待所有任务完成
    # # 启动前一定要关闭，保证不接收其他任务  # ValueError: Pool is still running
    # pool.close()
    # pool.join()
    # print(result.get())

    # imap
    # for result in pool.imap(get_html,[1,5,3]):
    #     # 按顺序打印
    #     print("{} sleep success" .format(result))

    # imap_unordered
    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        # 按完成顺序打印
        print("{} sleep success".format(result))
