<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [线程池](#%E7%BA%BF%E7%A8%8B%E6%B1%A0)
  - [线程池的使用](#%E7%BA%BF%E7%A8%8B%E6%B1%A0%E7%9A%84%E4%BD%BF%E7%94%A8)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 线程池

系统启动一个新线程的成本是比较高的，因为它涉及与操作系统的交互。在这种情形下，使用线程池可以很好地提升性能，尤其是当程序中需要创建大量生存期很短暂的线程时，更应该考虑使用线程池。

线程池在系统启动时即创建大量空闲的线程，程序只要将一个函数提交给线程池，线程池就会启动一个空闲的线程来执行它。当该函数执行结束后，该线程并不会死亡，而是再次返回到线程池中变成空闲状态，等待执行下一个函数。

此外，使用线程池可以有效地控制系统中并发线程的数量。当系统中包含有大量的并发线程时，会导致系统性能急剧下降，甚至导致 Python 解释器崩溃，而线程池的最大线程数参数可以控制系统中并发线程的数量不超过此数。



## 线程池的使用

线程池的基类是 concurrent.futures 模块中的 Executor，Executor 提供了两个子类，即 ThreadPoolExecutor 和 ProcessPoolExecutor，其中 ThreadPoolExecutor 用于创建线程池，而 ProcessPoolExecutor 用于创建进程池。
```python
# python3.9/concurrent/futures/thread.py
from concurrent.futures import _base

class ThreadPoolExecutor(_base.Executor):
```

Exectuor 提供了如下常用方法：

- submit(fn, *args, **kwargs)：将 fn 函数提交给线程池。*args 代表传给 fn 函数的参数，*kwargs 代表以关键字参数的形式为 fn 函数传入参数。
- map(func, *iterables, timeout=None, chunksize=1)：该函数类似于全局函数 map(func, *iterables)，只是该函数将会启动多个线程，以异步方式立即对 iterables 执行 map 处理。
- shutdown(wait=True)：关闭线程池。



Future 提供了如下方法：

- cancel()：取消该 Future 代表的线程任务。如果该任务正在执行，不可取消，则该方法返回 False；否则，程序会取消该任务，并返回 True。
- cancelled()：返回 Future 代表的线程任务是否被成功取消。
- running()：如果该 Future 代表的线程任务正在执行、不可被取消，该方法返回 True。
- done()：如果该 Future 代表的线程任务被成功取消或执行完成，则该方法返回 True。
- result(timeout=None)：获取该 Future 代表的线程任务最后返回的结果。如果 Future 代表的线程任务还未完成，该方法将会阻塞当前线程，其中 timeout 参数指定最多阻塞多少秒。
- exception(timeout=None)：获取该 Future 代表的线程任务所引发的异常。如果该任务成功完成，没有异常，则该方法返回 None。
- add_done_callback(fn)：为该 Future 代表的线程任务注册一个“回调函数”，当该任务成功完成时，程序会自动触发该 fn 函数。
