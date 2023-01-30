# global interpreter lock
# python中的一个线程是对应于c语言中的一个线程，一个线程在一个cpu上执行字节码,无法将多个线程映射到多个cpu上
# GIL IO操作频繁是高效的
import threading
from threading import Lock, RLock

# RLock 可重录的锁 在同一个线程里面，可以连续调用acquire,注意与释放的次数相等
# GIL 某些情况下会释放的,可能1000行字节码执行后会释放或者时间片后释放，或者I/o操作
total = 0
# 1.影响性能
# 2.会影响性能
# lock = Lock()
lock = RLock()


def add():
    # 1 dosomething 1
    # 2. IO 操作
    # 3. dosomething3
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total += 1
        lock.release()
        lock.release()


def sub():
    global total
    global lock
    for i in range(1000000):
        lock.acquire()
        lock.acquire()
        total -= 1
        lock.release()
        lock.release()


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=sub)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)
