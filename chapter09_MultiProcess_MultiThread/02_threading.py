from threading import Thread
import time


# 操作系统的调度最小单位为线程
# 对于io操作来说，多线程和多进程性能差别不大

# 网址 http://www.jobbole.com/caijing/gsyw/ 列表页
# 网址 http://www.jobbole.com/caijing/gsyw/168023.html  详情页


class GetDetailHtml(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail html starts")
        time.sleep(2)
        print("get detail html end")


class GetDetailUrl(Thread):
    def __init__(self, name):
        super().__init__(name=name)

    def run(self):
        print("get detail url starts")
        time.sleep(2)
        print("get detail url end")


def get_detail_html(url):
    print("get detail html starts\n")
    time.sleep(2)
    print("get detail html end\n")


def get_detail_url(url):
    print("get detail url starts\n")
    time.sleep(2)
    print("get detail url end\n")


if __name__ == "__main__":
    # 写法一：复杂
    # thread1 = Thread(target=get_detail_html,args=("",))
    # thread2 = Thread(target=get_detail_html,args=("",))
    # # 需求一： 当主线程结束后，子线程一并和主线程结束
    # # thread1.setDaemon(True)
    # # thread2.setDaemon(True)
    #
    # start_time = time.time()
    # thread1.start()
    # thread2.start()
    # # 需求二： 线程运行完之后再执行主线程
    # thread1.join()
    # thread2.join()
    #
    # print("last time:{}" .format(time.time()-start_time))

    # 写法二：简单
    thread1 = GetDetailHtml("get_detail_html")
    thread2 = GetDetailUrl("get_detail_url")
    start_time = time.time()
    thread1.start()
    thread2.start()
    #  主线程会等待所有的子线程结束后才结束
    thread1.join()
    thread2.join()
    print("last time:{}".format(time.time() - start_time))
