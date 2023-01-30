from multiprocessing import Process, Queue, Pool, Manager, Pipe

# from queue import Queue  错误：只能用在多线程

import time

# 多进程间不能用多线程的queue  会报错：can't pickle _thread.lock objects


def producer(queue):
    queue.put("a")
    time.sleep(2)


def consumer(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


# 共享全局变量


def producer1(a):
    a += 1
    time.sleep(2)


def consumer1(a):
    print(a)


def producer3(queue):
    queue.put("a")
    time.sleep(2)


def consumer3(queue):
    time.sleep(2)
    data = queue.get()
    print(data)


def producer4(pipe):
    pipe.send("danny")
    time.sleep(2)


def consumer4(pipe):
    time.sleep(2)
    data = pipe.recv()
    print(data)


def add_data(p_dict, key, value):
    p_dict[key] = value


if __name__ == "__main__":
    # queue
    # queue = Queue(10)
    # my_producer = Process(target=producer, args=(queue,))
    # my_consumer = Process(target=consumer, args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # 全局全局变量不适用于多进程编程
    # a = 1
    # my_producer = Process(target=producer1, args=(a,))
    # my_consumer = Process(target=consumer1, args=(a,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # multiprocessing中的queue不能用于pool进程池  输出为空
    # queue = Queue(10)
    # pool = Pool(2)
    # result_producer = pool.apply_async(producer3,args=(queue,))
    # result_consumer = pool.apply_async(consumer3,args=(queue,))
    # pool.close()
    # pool.join()

    # pool进程池  通讯需要使用manager中的Queue
    # queue = Manager().Queue(10)
    # pool = Pool(2)
    # result_producer = pool.apply_async(producer3,args=(queue,))
    # result_consumer = pool.apply_async(consumer3,args=(queue,))
    # pool.close()
    # pool.join()

    # 通过Pipe进行进程间通讯  2个
    # Pipe 的性能是高于queue，因为不是锁
    # receive_pipe, send_pipe = Pipe()
    # pip 只能适用于两个指定的进程
    # my_producer = Process(target=producer4, args=(send_pipe,))
    # my_consumer = Process(target=consumer4, args=(receive_pipe,))
    # my_producer.start()
    # my_consumer.start()
    # my_producer.join()
    # my_consumer.join()

    # 共享内存
    # 有常见的类型，list,array,value
    process_dict = Manager().dict()
    first_process = Process(target=add_data, args=(process_dict, "danny1", "haha"))
    second_process = Process(target=add_data, args=(process_dict, "danny2", "hehe"))
    first_process.start()
    second_process.start()
    first_process.join()
    second_process.join()
    print(process_dict)
