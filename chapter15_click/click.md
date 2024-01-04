<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [click](#click)
  - [Click 三个特点：](#click-%E4%B8%89%E4%B8%AA%E7%89%B9%E7%82%B9)
  - [基础函数](#%E5%9F%BA%E7%A1%80%E5%87%BD%E6%95%B0)
    - [装饰器 @click.option 通过指定命令行选项的名称，从命令行读取参数值，再将其传递给函数。其中，option 常用的设置参数如下：](#%E8%A3%85%E9%A5%B0%E5%99%A8-clickoption-%E9%80%9A%E8%BF%87%E6%8C%87%E5%AE%9A%E5%91%BD%E4%BB%A4%E8%A1%8C%E9%80%89%E9%A1%B9%E7%9A%84%E5%90%8D%E7%A7%B0%E4%BB%8E%E5%91%BD%E4%BB%A4%E8%A1%8C%E8%AF%BB%E5%8F%96%E5%8F%82%E6%95%B0%E5%80%BC%E5%86%8D%E5%B0%86%E5%85%B6%E4%BC%A0%E9%80%92%E7%BB%99%E5%87%BD%E6%95%B0%E5%85%B6%E4%B8%ADoption-%E5%B8%B8%E7%94%A8%E7%9A%84%E8%AE%BE%E7%BD%AE%E5%8F%82%E6%95%B0%E5%A6%82%E4%B8%8B)
  - [参考链接](#%E5%8F%82%E8%80%83%E9%93%BE%E6%8E%A5)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# click

Click是一个Python软件包，用于以可组合的方式创建漂亮的命令行界面，所需的代码更少。

## Click 三个特点：

- 命令的任意嵌套

- 自动帮助页面生成

- 支持在运行时延迟加载子命令

## 基础函数
- 使用@click.command() 装饰一个函数，使之成为命令行接口
- 使用@click.option() 装饰函数，为其添加命令行选项
- 使用@click.argument()装饰函数，为其添加命令行选项

### 装饰器 @click.option 通过指定命令行选项的名称，从命令行读取参数值，再将其传递给函数。其中，option 常用的设置参数如下：
- default 设置命令行参数的默认值；
- help 参数说明；
- type 指定参数类型，如 string int float ；
- prompt 当命令行未指定相应参数时，会根据 prompt 提示用户输入；
- nargs 指定命令行参数接受的值的个数。


## 参考链接
1. [官方](https://click.palletsprojects.com/en/8.0.x/)