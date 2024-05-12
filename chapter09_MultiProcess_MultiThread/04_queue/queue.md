<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Queue 模块](#queue-%E6%A8%A1%E5%9D%97)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Queue 模块
Queue 模块可以实现多生产者与多消费者队列，它可以实现多个线程之间的信息安全交换。



它有几种队列模式：

- FIFO队列，先进先出
```python
q = queue.Queue(10)  # FIFO 队列，最多放入10个项目
q.put(123) # 队列中存入项目123
```
- LIFO队列，后进先出，如同栈

```python
q = queue.LifoQueue()   # LIFO 队列，项目数无限 
q.put(123) # 队列中存入项目123
```

- Priority队列，对着中的数据始终保持排序，优先检索最低值。 通常使用 (优先序号, 数据)形式存储数据。不带需要默认对其值进行排序。

```python
q = queue.PriorityQueue(10) # Priority 队列，最多放入10个项目
q.put((1,'a')) # 队列中存入项目(1,'a')
```


如果设置的maxsize小于1，则表示队列的长度无限长


- Queue.task_done()　　从场景上来说，处理完一个get出来的item之后，调用task_done将向队列发出一个信号，表示本任务已经完成

- Queue.join()　　监视所有item并阻塞主线程，直到所有item都调用了task_done之后主线程才继续向下执行。这么做的好处在于，假如一个线程开始处理最后一个任务，它从任务队列中拿走最后一个任务，此时任务队列就空了但最后那个线程还没处理完。当调用了join之后，主线程就不会因为队列空了而擅自结束，而是等待最后那个线程处理完成了。