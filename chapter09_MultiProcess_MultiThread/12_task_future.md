<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [tasks 是协程与future的桥梁](#tasks-%E6%98%AF%E5%8D%8F%E7%A8%8B%E4%B8%8Efuture%E7%9A%84%E6%A1%A5%E6%A2%81)
- [task 负责启动协程，并且StopIteration时把结构放在set_result中](#task-%E8%B4%9F%E8%B4%A3%E5%90%AF%E5%8A%A8%E5%8D%8F%E7%A8%8B%E5%B9%B6%E4%B8%94stopiteration%E6%97%B6%E6%8A%8A%E7%BB%93%E6%9E%84%E6%94%BE%E5%9C%A8set_result%E4%B8%AD)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# tasks 是协程与future的桥梁

# task 负责启动协程，并且StopIteration时把结构放在set_result中
