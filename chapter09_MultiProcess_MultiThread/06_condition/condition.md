<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Condition 条件变量](#condition-%E6%9D%A1%E4%BB%B6%E5%8F%98%E9%87%8F)
  - [场景](#%E5%9C%BA%E6%99%AF)
  - [方法](#%E6%96%B9%E6%B3%95)
  - [处理流程](#%E5%A4%84%E7%90%86%E6%B5%81%E7%A8%8B)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Condition 条件变量

## 场景

线程A需要等某个条件成立才能继续往下执行，现在这个条件不成立，线程A就阻塞等待，而线程B在执行过程中使这个条件成立了，就唤醒线程A继续执行


## 方法
Condition.wait([timeout])　　这个方法一定要在获取锁定之后调用，调用这个方法的Condition对象所在的线程会被挂起并且释放这个线程获得着的所有锁，直到接到通知被唤醒或者超时（如果设置了Timeout的话），当被唤醒之后线程将重新获取锁定。

Condition.notify()　　notify就是上面所说的通知，调用这个方法之后会唤醒一个被挂起的线程。线程的选择尚不明确，似乎是随机的。需要注意的是notify方法只进行挂起的唤醒而不涉及锁的释放

Condition.notify_all()　　唤醒所有挂起的线程


## 处理流程
- 首先acquire一个条件变量，然后判断一些条件。
- 如果条件不满足则wait；
- 如果条件满足，进行一些处理改变条件后，通过notify方法通知其他线程，其他处于wait状态的线程接到通知后会重新判断条件。
- 不断的重复这一过程，从而解决复杂的同步问题