# 通过queue的方式进行线程间通信
from queue import Queue
from threading import Thread
import time

# 线程安全的，底层queue的结构是deque双端队列，字节码级别线程安全


def get_detail_html(queue):
    while True:
        url = queue.get()
        print("get detail html:{url} starts".format(url=url))
        time.sleep(2)
        print("get detail html:{url}end".format(url=url))


def get_detail_url(queue):
    # 爬取文章列表页
    while True:
        print("get detail url starts")
        time.sleep(2)
        for i in range(20):
            queue.put("http://projectedu.com/{id}".format(id=i))
        print("get detail url end")


if __name__ == "__main__":
    url_queue = Queue(maxsize=1000)
    thread_detail_url = Thread(target=get_detail_url, args=(url_queue,))
    for i in range(10):
        html_thread = Thread(target=get_detail_html, args=(url_queue,))
        html_thread.start()
    thread_detail_url.start()
    # 结束 以下成对
    url_queue.task_done()
    url_queue.join()
