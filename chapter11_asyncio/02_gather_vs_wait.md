<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [gather和wait方法的区别](#gather%E5%92%8Cwait%E6%96%B9%E6%B3%95%E7%9A%84%E5%8C%BA%E5%88%AB)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# gather和wait方法的区别


- gather具有把普通协程函数包装成协程任务的能力，wait没有。wait只能接收包装后的协程任务列表做参数。
- 两者返回值不一样，wait返回的是已完成和未完成任务的列表，而gather直接返回协程任务执行结果。
- gather返回的任务执行结果是有序的，wait方法获取的结果是无序的