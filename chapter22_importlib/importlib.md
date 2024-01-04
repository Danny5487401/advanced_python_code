<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [importlib](#importlib)
  - [动态导入](#%E5%8A%A8%E6%80%81%E5%AF%BC%E5%85%A5)
  - [模块导入检查](#%E6%A8%A1%E5%9D%97%E5%AF%BC%E5%85%A5%E6%A3%80%E6%9F%A5)
  - [从源代码导入](#%E4%BB%8E%E6%BA%90%E4%BB%A3%E7%A0%81%E5%AF%BC%E5%85%A5)
  - [参考资料](#%E5%8F%82%E8%80%83%E8%B5%84%E6%96%99)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# importlib


## 动态导入
importlib模块支持传递字符串来导入模块

## 模块导入检查
Python有个众所周知的代码风格EAFP: Easier to ask forgiveness than permission.它所代表的意思就是总是先确保事物存在(例如字典中的键)以及在犯错时捕获。如果我们在导入前想检查是否这个模块存在而不是靠猜

## 从源代码导入
可以使用util通过模块的名字和路径来导入模块。


## 参考资料

