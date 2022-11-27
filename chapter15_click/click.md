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