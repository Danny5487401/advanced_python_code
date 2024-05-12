<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [信号量(Semaphore)](#%E4%BF%A1%E5%8F%B7%E9%87%8Fsemaphore)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# 信号量(Semaphore)

信号量是一个内部数据，它有一个内置的计数器，它标明当前的共享资源可以有多少线程同时读取。


信号量控制规则：当计数器大于0时，那么可以为线程分配资源权限；当计数器小于0时，未获得权限的线程会被挂起，直到其他线程释放资源

