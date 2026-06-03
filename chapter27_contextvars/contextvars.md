<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [contextvars](#contextvars)
  - [参考](#%E5%8F%82%E8%80%83)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# contextvars

`contextvars` 用于在异步任务中保存上下文变量。它适合传递请求 ID、用户标识、链路追踪 ID 等不希望显式层层传参、但又需要在不同协程任务之间隔离的数据。

## 参考
- [上下文管理](https://www.cnblogs.com/traditional/p/11253644.html)
