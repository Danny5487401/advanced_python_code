<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [异步编程](#%E5%BC%82%E6%AD%A5%E7%BC%96%E7%A8%8B)
  - [基本概念](#%E5%9F%BA%E6%9C%AC%E6%A6%82%E5%BF%B5)
  - [消息通用机制](#%E6%B6%88%E6%81%AF%E9%80%9A%E7%94%A8%E6%9C%BA%E5%88%B6)
  - [总结：](#%E6%80%BB%E7%BB%93)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# 异步编程
## 基本概念
- 并发：高并发  指一个时间段内，有几个程序在一个cpu中，但是任意时刻只有一个程序在运行，类似操作系统
- 并行：在任意时刻上，有多个程序运行到多个cpu上

## 消息通用机制
-  同步：代码调用Io操作时，必须等待IO操作完成后才返回的调用方式
-  异步：代码调用Io操作时，不必等待IO操作完成后才返回的调用方式

-  阻塞：调用函数时当前线程被挂起
-  非阻塞：调用函数时当前线程不被挂起，立马返回


## 总结：
1. 并行是为了利用多核加速多任务完成的进度
2. 并发是为了让独立的子任务都有机会被尽快执行，但不一定能加速整体进度
3. 非阻塞是为了提高程序整体执行效率
4. 异步是高效地组织非阻塞任务的方式

异步编程： 以进程、线程、协程、函数/方法作为执行任务程序的基本单位，结合回调、事件循环、信号量等机制，以提高程序整体执行效率和并发能力的编程方式。
