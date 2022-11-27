
# argparse

argparse 是一个用来解析命令行参数的 Python 库


## 使用
argparse使用主要有四个步骤：

1. 导入argparse包
2. 创建 ArgumentParser() 参数对象
3. 调用 add_argument() 方法往参数对象中添加参数
4. 使用 parse_args() 解析添加参数的参数对象，获得解析对象
5. 程序其他部分，当需要使用命令行参数时，使用解析对象.参数获取
