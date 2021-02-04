# global interpreter lock
# python中的一个线程是对应于c语言中的一个线程，一个线程在一个cpu上执行字节码,无法将多个线程映射到多个cpu上
# GIL IO操作频繁是高效的
import threading
# GIL 某些情况下会释放的,可能1000行字节码执行后会释放或者时间片后释放，或者I/o操作
total = 0


def add():
    # 1 dosomething 1
    # 2. IO 操作
    # 3. dosomething3
    global total
    for i in range(1000000):
        total += 1


def sub():
    global total
    for i in range(1000000):
        total -= 1


thread1 = threading.Thread(target=add)
thread2 = threading.Thread(target=sub)
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print(total)
# import dis
# def add(a):
#     a = a+1
#     return a
#
#
# print(dis.dis(add))
"""
  5           0 LOAD_FAST                0 (a)
              2 LOAD_CONST               1 (1)
              4 BINARY_ADD
              6 STORE_FAST               0 (a)

  6           8 LOAD_FAST                0 (a)
             10 RETURN_VALUE
None
"""