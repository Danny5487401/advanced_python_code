# contextvars

`contextvars` 用于在异步任务中保存上下文变量。它适合传递请求 ID、用户标识、链路追踪 ID 等不希望显式层层传参、但又需要在不同协程任务之间隔离的数据。

## 参考
- [上下文管理](https://www.cnblogs.com/traditional/p/11253644.html)
