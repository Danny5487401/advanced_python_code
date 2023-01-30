import dis


def add(a, b):

    return a + b


print(dis.dis(add))
"""
  6           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
None



在输出的结果中一共四行:

1. 前两行操作码都是LOAD_FAST, 加载了两个不同的变量
2. 第三行是执行加法运算的操作码: BINARY_ADD
3. 最后一行是返回值的操作码: RETURN_VALUE，每个函数都会有这个操作码，即使你没有写return语句
"""
