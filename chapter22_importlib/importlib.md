# importlib


## 动态导入
importlib模块支持传递字符串来导入模块

## 模块导入检查
Python有个众所周知的代码风格EAFP: Easier to ask forgiveness than permission.它所代表的意思就是总是先确保事物存在(例如字典中的键)以及在犯错时捕获。如果我们在导入前想检查是否这个模块存在而不是靠猜

## 从源代码导入
可以使用util通过模块的名字和路径来导入模块。
