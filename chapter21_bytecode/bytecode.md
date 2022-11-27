# 字节码(ByteCode)


python运行代码时候的基本逻辑: 
第一步: python解释器会将你写的python代码先编译为字节码
第二步: 当你每一次调用函数，或者刚开始运行python的时候，cpython会建立一个新的Frame，然后在这个Frame框架下，cpython会一条一条的执行编译后的ByteCode, 每一条ByteCode在C语言中有相应的代码去执行它。


## CPython 虚拟机内幕

cpython中处理与字节码有关的文件是：Python/ceval.c， 对应的头文件路径:Include/ceval.h

CPython 使用一个基于栈的虚拟机。也就是说，它完全面向栈数据结构的（你可以 “推入” 一个东西到栈 “顶”，或者，从栈 “顶” 上 “弹出” 一个东西来）。

CPython 使用三种类型的栈：

- 调用栈call stack。这是运行 Python 程序的主要结构。它为每个当前活动的函数调用使用了一个东西 —— “帧frame”，栈底是程序的入口点。每个函数调用推送一个新的帧到调用栈，每当函数调用返回后，这个帧被销毁。
- 在每个帧中，有一个计算栈evaluation stack （也称为数据栈data stack）。这个栈就是 Python 函数运行的地方，运行的 Python 代码大多数是由推入到这个栈中的东西组成的，操作它们，然后在返回后销毁它们。
- 在每个帧中，还有一个块栈block stack。它被 Python 用于去跟踪某些类型的控制结构：循环、try / except 块、以及 with 块，全部推入到块栈中，当你退出这些控制结构时，块栈被销毁。这将帮助 Python 了解任意给定时刻哪个块是活动的，比如，一个 continue 或者 break 语句可能影响正确的块

案例： my_function(my_variable, 2)

Python 将转换为一系列字节码指令：
1. 一个 LOAD_NAME 指令去查找函数对象 my_function，然后将它推入到计算栈的顶部
2. 另一个 LOAD_NAME 指令去查找变量 my_variable，然后将它推入到计算栈的顶部
3. 一个 LOAD_CONST 指令去推入一个实整数值 2 到计算栈的顶部
4. 一个 CALL_FUNCTION 指令


