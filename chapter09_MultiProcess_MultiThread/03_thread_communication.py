from threading import Thread
import time

# 推荐线程安全的 queue

# 线程间的通讯方式，共享变量
# 全局变量方式
# detail_url_list = []
# def get_detail_html():
#     # 爬取文章详情页
#     global detail_url_list
#     # 不合理，并发低
#     # for url in detail_url_list:
#     #     print("get detail html starts")
#     #     time.sleep(2)
#     #     print("get detail html end")
#     # 方法二
#     url = detail_url_list.pop()
#     print("get detail html starts")
#     time.sleep(2)
#     print("get detail html end")
#
# def get_detail_url():
#     # 爬取文章列表页
#     print("get detail url starts")
#     time.sleep(2)
#     global detail_url_list
#     for i in range(20):
#         detail_url_list.append("http://projectedu.com/{id}") .format(id = i)
#
#     print("get detail url end")

# 灵活方式
# detail_url_list = []
# def get_detail_html(detail_url):
#     # 爬取文章详情页
#     # 不合理，并发低
#     # for url in detail_url_list:
#     #     print("get detail html starts")
#     #     time.sleep(2)
#     #     print("get detail html end")
#     # 方法二
#     while True:
#         if len(detail_url):
#             url = detail_url.pop()
#             print("get detail html:{url} starts" .format(url=url))
#             time.sleep(2)
#             print("get detail html:{url}end".format(url=url))
#
# def get_detail_url(detail_url):
#     # 爬取文章列表页
#     while True:
#         print("get detail url starts")
#         time.sleep(2)
#         for i in range(20):
#             detail_url.append("http://projectedu.com/{id}" .format(id=i))
#         print("get detail url end")


# 外界变量
from chapter09_MultiProcess_MultiThread import variable


def get_detail_html():
    while True:
        if len(variable.detail_url_list):
            url = variable.detail_url_list.pop()
            print("get detail html:{url} starts".format(url=url))
            time.sleep(2)
            print("get detail html:{url}end".format(url=url))


def get_detail_url():
    # 爬取文章列表页
    while True:
        print("get detail url starts")
        time.sleep(2)
        for id in range(20):
            variable.detail_url_list.append("http://projectedu.com/{id}".format(id=id))
        print("get detail url end")


if __name__ == "__main__":
    detail_url_list = []
    # thread_detail_url = Thread(target=get_detail_url)
    # for i in range(10):
    #     html_thread = Thread(target= get_detail_html)
    #     html_thread.start()
    # thread_detail_url.start()

    # thread_detail_url = Thread(target=get_detail_url,args=(detail_url_list,))
    # for i in range(10):
    #     html_thread = Thread(target= get_detail_html,args=(detail_url_list,))
    #     html_thread.start()
    # thread_detail_url.start()

    thread_detail_url = Thread(target=get_detail_url)
    for i in range(10):
        html_thread = Thread(target=get_detail_html)
        html_thread.start()
    thread_detail_url.start()
