import threading

# semaphore 用于控制进入数量的锁
# 文件：读和写 ，写就一个线程，读可以允许有多个线程

# 控制爬虫的数量
import time


class HtmlSpider(threading.Thread):
    def __init__(self, url, sem):
        super().__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print("got html text success")
        # 注意释放的位置
        self.sem.release()  # 释放共享资源，信号量计数器+1


class UrlProducer(threading.Thread):
    def __init__(self, sem):
        super().__init__()
        self.sem = sem

    def run(self):
        for i in range(10):
            self.sem.acquire()  # 获取共享资源，信号量计数器-1
            html_thread = HtmlSpider("https://www.baidu.com/{}".format(i), self.sem)
            html_thread.start()


if __name__ == "__main__":
    sem = threading.Semaphore(3)  # 创建信号量对象，5个线程并发
    url_producer = UrlProducer(sem)
    url_producer.start()
