<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [pytest](#pytest)
  - [用例编写规范](#%E7%94%A8%E4%BE%8B%E7%BC%96%E5%86%99%E8%A7%84%E8%8C%83)
  - [pytest-mock 插件](#pytest-mock-%E6%8F%92%E4%BB%B6)
  - [命令行使用](#%E5%91%BD%E4%BB%A4%E8%A1%8C%E4%BD%BF%E7%94%A8)
    - [-k EXPRESSION](#-k-expression)
    - [-x, --exitfirst](#-x---exitfirst)
    - [-m MARKEXPR](#-m-markexpr)
  - [参考](#%E5%8F%82%E8%80%83)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->


# pytest 

pytest是基于unittest衍生出来的新的测试框架，使用起来相对于unittest来说更简单、效率来说更高，pytest兼容unittest测试用例，但是反过来unittest不兼容pytest。


## 用例编写规范

- 测试文件以test_开头(或者以_test结尾)
pytest会找当前以及递归查找子文件夹下面所有的test_*.py或*_test.py的文件，把其当作测试文件（除非显式指定文件所在路径）

- 测试类名称以Test开头，并且不能带有init方法
如果类名称以Test开头的class类中包含了init方法，则会触发告警，提示PytestCollectionWarning: cannot collect test class 'TestXXX'
- 测试函数以test_开头
- 断言使用基本的assert即可


## pytest-mock 插件


## 命令行使用
```shell
✗ pytest --help                 
usage: pytest [options] [file_or_dir] [file_or_dir] [...]

positional arguments:
  file_or_dir
# ...
```

### -k EXPRESSION
使用该参数可以指定运行满足要求的用例。用法如下
```shell
pytest -k "类名"
pytest -k "方法名"
pytest -k "类名 and not 方法名"
```

### -x, --exitfirst
遇到用例执行失败或断言失败，立即停止运行，不执行后面的用例


###  -m MARKEXPR
按照标签名运行所有包含某个标签的用例，需要在测试用例上面都加上装饰符@pytest.mark.标记名。
使用-m选项，可以使表达式指定多个标记名。使用-m "mark1 and mark2"可以同时选中带有这两个标记的所有测试用例。

使用-m "mark1 and  not mark2"则会选中带mark1标记且不带mark2标记的测试用例，

使用-m "mark1 or mark2"则会选中带有mark1或者mark2的所有测试用例


## 参考
- [官方 pytest 文档](https://docs.pytest.org/en/8.1.x/)
