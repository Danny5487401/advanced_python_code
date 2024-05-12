<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [GIL（Global Interpreter Lock 全局解释器锁）](#gilglobal-interpreter-lock-%E5%85%A8%E5%B1%80%E8%A7%A3%E9%87%8A%E5%99%A8%E9%94%81)
  - [GIL为Python解决了什么问题](#gil%E4%B8%BApython%E8%A7%A3%E5%86%B3%E4%BA%86%E4%BB%80%E4%B9%88%E9%97%AE%E9%A2%98)
  - [是不是python的多线程就完全没用了呢？](#%E6%98%AF%E4%B8%8D%E6%98%AFpython%E7%9A%84%E5%A4%9A%E7%BA%BF%E7%A8%8B%E5%B0%B1%E5%AE%8C%E5%85%A8%E6%B2%A1%E7%94%A8%E4%BA%86%E5%91%A2)
  - [如何避免 GIL](#%E5%A6%82%E4%BD%95%E9%81%BF%E5%85%8D-gil)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->



# GIL（Global Interpreter Lock 全局解释器锁）


这是在实现 CPython（Python 解释器）时引入的一个概念。我们可以将 GIL 理解为一个互斥锁，用于保护 Python 中的对象，防止多个线程同时执行 Python 字节码，从而确保线程安全。

GIL 有一个缺点，那就是一次只有一个线程能在一个 CPU 上执行，多个线程无法映射到多个 CPU，因此 Python 无法实现真正的多线程并发，从而降低了执行效率


## GIL为Python解决了什么问题

GIL的引入是为了解决CPython解释器的线程安全问题。由于CPython的内存管理并不是线程安全的，如果多个线程同时执行Python字节码，可能会导致数据竞争和内存错误。
为了解决这个问题，GIL被引入，并确保了同一时间只有一个线程可以执行Python字节码，从而消除了竞争条件。

引用计数变量需要保护竞争条件。如果其中两个线程同时增加或减少其值，如果发生这种情况，它可能导致从未释放的内存泄漏，或者更糟糕的是，在对该对象的引用仍然存在时错误地释放内存。
这可能会导致Python程序中出现崩溃或其他“怪异”错误。通过向跨线程共享的所有数据结构添加锁，可以保持此引用计数变量的安全性，从而不会对它们进行不一致的修改。


GIL是解释器本身的单个锁，它增加了一条规则，即执行任何Python字节码都需要获取解释器锁。这可以防止死锁（因为只有一个锁）并且不会引入太多的性能开销。
但它有效地使任何受CPU限制的Python程序都是单线程的


## 是不是python的多线程就完全没用了呢？


分类讨论：

1、CPU密集型代码(各种循环处理、计数等等)，在这种情况下，ticks计数很快就会达到阈值，然后触发GIL的释放与再竞争（多个线程来回切换当然是需要消耗资源的），所以python下的多线程对CPU密集型代码并不友好。

2、IO密集型代码(文件处理、网络爬虫等)，多线程能够有效提升效率(单线程下有IO操作会进行IO等待，造成不必要的时间浪费，而开启多线程能在线程A等待时，自动切换到线程B，可以不浪费CPU的资源，从而能提升程序执行效率)。所以python的多线程对IO密集型代码比较友好。



## 如何避免 GIL

- 使用 multiprocess
- 使用其他 Interpreter，比如说 Jython、IronPython 或 PyPy。
- Python 官方移除 GIL：
  - https://discuss.python.org/t/a-steering-council-notice-about-pep-703-making-the-global-interpreter-lock-optional-in-cpython/30474
  - https://peps.python.org/pep-0703/




