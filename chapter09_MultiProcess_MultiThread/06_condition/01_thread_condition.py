import threading

# condition的应用有  queue.Queue

# 条件变量，用于复杂的线程间同步

# 对话：
"""
xiaomi: hello,danny
xiaoai: hello, joy

xiaomi: how r u?
xiaoai: i am fine!

xiaomi: what is yr job?
xiaoai: i am a teacher
"""

# 这种方式不行：一次性读完
# class XiaoAi(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name="小爱")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}:hello, joy" .format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{}:i am fine!" .format(self.name))
#         self.lock.release()
#
# class XiaoMi(threading.Thread):
#     def __init__(self,lock):
#         super().__init__(name="小米")
#         self.lock = lock
#
#     def run(self):
#         self.lock.acquire()
#         print("{}:hello,danny" .format(self.name))
#         self.lock.release()
#
#         self.lock.acquire()
#         print("{}:how r u?".format(self.name))
#         self.lock.release()


class XiaoAi(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="小爱")
        self.cond = condition

    def run(self):
        with self.cond:
            self.cond.wait()
            print("{}:hello, joy".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:i am fine!".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:i am a teacher".format(self.name))
            self.cond.notify()


class XiaoMi(threading.Thread):
    def __init__(self, condition):
        super().__init__(name="小米")
        self.cond = condition

    def run(self):
        with self.cond:
            print("{}:hello,danny".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:how r u?".format(self.name))
            self.cond.notify()

            self.cond.wait()
            print("{}:what is yr job?".format(self.name))
            self.cond.notify()


if __name__ == "__main__":
    condition = threading.Condition()
    xiaomi = XiaoMi(condition)
    xiaoai = XiaoAi(condition)
    # 注意启动顺序
    # xiaomi.start()
    # xiaoai.start()
    # 正确的启动方式
    # condition有两把锁，一把底层锁在wait()调用后释放，上面的锁会在每次调用wait时候分配一把并放入cond的等待队列deque中,等待Notify的唤醒
    xiaoai.start()
    xiaomi.start()
